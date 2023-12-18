# OpenAreaText
Open Source area codes and locale API for SMS messaging and marketing companies. 

API docs:  http://www.openareatext.com/apidocs/

API architecture/overview: 



# The Problem 

SMS companies do not have a ground source of truth when it comes to updating area codes, timezones, and other locale data, often storing and updatng this data manually in local files. At best, this results in annoyances for engineering teams that have to manually update area codes and locale data to match NANP and other federal agency guidelines in an enum or databases. At worst, this can lead to critical SMS delievery failures to customers. 

# The Solution 

This open-source programmatic API can fetch real-time locale data that will be automatically refreshed and updated as time goes on. For now, I am starting with area codes. The result of this is that  companies can spend less time worrying about whether their locale data is updated for messaging and more time shipping impactful features for their customers. The flexibility of this API can allow companies to use this as a ground source of truth for locale data or plug this api into your unit or integration tests so that engineers are aware of potential changes upcoming for locale data. 

# Current Notable Users (please see below for who we'd love to bring onto this project!)

# Roadmap/Asks (How you can help!)

- Scraping area code data using beautifulsoup off of Allareacodes and/or Wikipedia's NANP page ✅
- Working endpoints for neccesary area codes use cases ✅
- A fast DB store to read and write new data (Suspended, due to high compute costs. For now I am passing in the scraped dictionary manually)
- Basic Security (rate limiting, validation, etc)✅
- Contacts to engineers and engineering teams at the following companies: Attentive, PostScript, Telnyx, Twilio, Wizard SMS


 
