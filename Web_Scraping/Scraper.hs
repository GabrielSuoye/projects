{-# LANGUAGE OverloadedStrings #-}

module Main where

import Network.HTTP.Simple (httpLBS, parseRequest, getResponseBody)
import Text.HTML.TagSoup (parseTags, Tag(..))
import Data.Text (Text)
import qualified Data.Text as T
import qualified Data.Text.Encoding as TE
import qualified Data.ByteString.Lazy as LBS

-- | The URL we want to scrape
targetUrl :: String
targetUrl = "https://news.ycombinator.com"

main :: IO ()
main = do
    putStrLn $ "Fetching URL: " ++ targetUrl
    
    -- 1. Create a request object from the URL string
    request <- parseRequest targetUrl
    
    -- 2. Download the HTML content using http-conduit
    response <- httpLBS request
    let htmlByteString = getResponseBody response
    
    -- 3. Decode the lazy ByteString into Text (UTF-8)
    let htmlText = TE.decodeUtf8 (LBS.toStrict htmlByteString)
    
    -- 4. Parse the HTML text into a flat list of TagSoup tags
    let tags = parseTags htmlText
    
    -- 5. Extract article titles from Hacker News layout
    -- HN articles look like: <span class="titleline"><a href="...">Title Here</a></span>
    let titles = extractHNTitles tags
    
    -- 6. Print out the results
    putStrLn "\n--- Extracted Titles ---"
    mapM_ (putStrLn . T.unpack) titles

-- | Helper function to parse TagSoup tags and pull text inside <span class="titleline"><a...>
extractHNTitles :: [Tag Text] -> [Text]
extractHNTitles [] = []
extractHNTitles (TagOpen "span" attrs : ts)
    | hasClass "titleline" attrs = 
        -- If we find <span class="titleline">, look for the text inside the nested <a> tag
        case findAnchorText ts of
            Just (title, remainingTags) -> title : extractHNTitles remainingTags
            Nothing                     -> extractHNTitles ts
    | otherwise = extractHNTitles ts
extractHNTitles (_ : ts) = extractHNTitles ts

-- | Check if an element attribute list contains the target class
hasClass :: Text -> [(Text, Text)] -> Bool
hasClass className attrs = case lookup "class" attrs of
    Just val -> className `elem` T.words val
    Nothing  -> False

-- | Look ahead in the tags list to extract the text inside the <a> tag
findAnchorText :: [Tag Text] -> Maybe (Text, [Tag Text])
findAnchorText (TagOpen "a" _ : TagText titleText : ts) = Just (titleText, ts)
findAnchorText (_ : ts)                                 = findAnchorText ts
findAnchorText []                                       = Nothing
