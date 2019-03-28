# Notes

## Settings
You should be aware of what the `settings.py` file is for.

In general, `ROBOTSTXT_OBEY = True` to ensure you aren't annoying the owners of the site you're scraping.

Along the same lines, `CONCURRENT_REQUESTS` and `DOWNLOAD_DELAY` are useful for ensuring you do not overload the target website with requests.

Large sites often require your spider to identify itself. That's what `USER_AGENT` is for. You can get yours by going [here](https://www.whoishostingthis.com/tools/user-agent/) and assigning the relevant text under *Your User Agent is:* as a string to `USER_AGENT`.



