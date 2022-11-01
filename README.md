# Twitter-Tweet-Alert-System

## Introduction

Tweeter users typically follow multiple Twitter accounts. Keeping track of all postings, updates, and trends is thus difficult, and important announcement tweets from Google Search accounts may be missed. To address this, I'll use Python to build a simple Twitter alert system that uses the Python module Advertools to connect to the Twitter API and scan the current day's posts of specific accounts for keywords of interest. If a match is found, an email alert will be sent to ensure he/she never misses another core update announcement.

### Requirements

**advertools**: For the Twitter API connection

**pandas**: To handle the dataframe response from advertools

**datetime**: To grab today’s date for the Twitter date range

**yagmail**: To send the email alert