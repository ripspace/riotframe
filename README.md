**RiotFrame V1: The revolution will be livestreamed.**

A video streaming tool for art and activist: works on Twitch, Youtube, DailyMotion, and any other streameer that accepts rtmp video streams.
Streams a set of videos from a directory to any streamer 24 hours 7 days a week till either someone kills it, gets flagged or the system gets disabled.

Some ideas on how to use it:  
A] Setup am art,  protest or counter programming stream that runs video content 24/7days a week indefinitely.
    The longer a stream runs, the more the algoryhtm will prioritized it.  
B] Set up multiple instances to stream to a service and take over an entire subject/cateogory:  
   I.E. Insert name of target subject, hashtag or livesteamer's name 10-20 streams  
   the same title/name and take over expose their audience to counter programming.  
C] CultureJamming: Stream content people are searching for and mix it with counter programming.  
D] Rat ***ing, stream cloning , and other advanced trouble can also be done or implemented.  
E] Many more users , but it's up to you how to flex it.  

Current Features

Endless Looping: Keep your stream going with infinite video loops. No breaks, no interruptions.

Text Overlays: Add your own titles to videos with an optional overlay—fully configurable, completely customizable.

Stream Anywhere: Whether it's YouTube, Dailymotion, or any other RTMP destination

Zero Dependencies: Forget about complex setups and databases. Just a simple, powerful tool to stream your content without limits.

Complete Control: Stream videos from a local directory, with titles read from a text file. Loop through your media and keep the message going.

Use Case:
Activists: Stream protest footage and calls to action with encrypted RTMP support.
Rebels: Want to control the narrative? RiotFrame gives you the tools to fight back.
Creators: Whether it's your art, your message, or your voice, RiotFrame gives you the platform to broadcast without censorship.

How It Works

Set up your stream URL: Define the destination—whether you're streaming to Dailymotion, YouTube, or any RTMP server.
E
nable text overlays: Turn on the text overlay for each video, adding a title or message on the fly.
Feed your directory: Place your videos in the specified folder. The tool will loop through them and stream them endlessly.
Watch the chaos unfold: Press play and broadcast your message to the world.
Get Started
Clone the repo, configure your settings at the top of file and get motherfucking busy.

Setup Instructions:
Clone the repository:

```
bash
    git clone https://github.com/ripspace/riotframe.git
    cd riotframe
```

Configure the stream settings: Set your RTMP stream URL, toggle text overlays, and point to your video directory and title file in the config section at the top of the script.


Run the script:

```
bash
    python riotframe.py
    Stop the stream: Hit Ctrl+C to gracefully stop.
```


```
Run Headleass and in the bakground
    nohup python riotframe.py &
```
    
