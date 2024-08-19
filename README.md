# seterra bot

## what the fuck is this? 
so, you know that seterra game made by the cunts who made geoguessr where they make you find all 50 us states or countries or whatever like some kind of geographic torture? yeah, fuck that. this bot does it for you because life's too short to be clicking on montana when you could be doing literally anything else. (this only works on the US states)

## how does it work? 
alright, this piece of shit uses `playwright` to open a browser, heads over to the seterra page, and starts clicking those states like it’s on crack. it even adjusts for louisiana and michigan’s bullshit hitboxes because, let’s be honest, nothing about this country is straightforward, not even the goddamn maps.

## setup & run 🚀
1. **get your shit together:**
   - first, make sure python’s up and running.
   - then, run `pip install colorama playwright` like a good little nerd
   - don’t forget to set up playwright: `playwright install`

2. **run the bot:**
   - clone the repo (if you can’t figure this out, just quit now):
     ```
     git clone https://github.com/LiterallyAxo/SeterraBot.git
     cd SeterraBot
     ```
   - run the bot with an optional delay (because sometimes you need to pretend you actually paid attention in history class):
     ```
     python bot.py [delay]
     ```
     *example:* `python bot.py 0` (because slow and steady wins absolutely fucking nothing)

3. **watch it click those states like a horny teenager on a dating app**. after 50 clicks, it’s done, just like my motivation after a long week of dealing with people’s bullshit.

## the code 💻
this was slapped together with minimal effort, because who’s got time for perfection? the bot goes to the game, scrolls down like it’s trying to find the good part in a bad porno, then waits for the instructions like a good little slave. it clicks, counts, and after 50, it’s out faster than me at a boring family reunion. if this hellhole of a country gets another state this is going to break though, if you couldnt tell my coding skills are unmatched.

there’s some logging too, so you can watch the bot in action and feel superior to your browser for once. oh, and if you close the browser window, the bot will just fuck off and die. simple as that.

## license 📄
this is under the gnu license. do whatever the fuck you want with it, just don’t come crying to me if it breaks something or if your life is still just as empty after using it.
