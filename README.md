# YoutubeScrapper

  1. Get Video link & number(n).
  2. Extract n video_ids using link, if correct link then extract channel name & unique url.
  3. Check in database(Azure-SQL) and create unique table for channel(channel_name_url) if not present.
  4. Extract Video_link and Total_likes,title,thumbnail_url,Total_Views for each Video_link.
  5. Check Channel table and insert above details for each Video_Id if not present, if present then Update Total_likes & Views.
  6. Returned latest extracted details and database details to show on next page.
  7. It will take longer time to show result if n is larger.
