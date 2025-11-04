# Fri Aug 29
## Engineering Journal

I'm planning on using this journal to document my personal projects, school assignments, and aspirational projects.

Personal projects are ones which I must complete for the sake of some non-academic interest; whether that be pure experimental curiosity or some professional requirement.

School assignments are self-descriptive; whatever tasks I should accomplish for course work.

Aspirational projects are ones that I have not started but seem like cool ideas to me.


The personal project I'm currently working on is a Scratch VM that I can use to run scratch projects on embedded hardware, namely an esp32.
I'm currently struggling with it, and it's hard to even put my finger on why. I think I'm floundering a bit when it comes to identifying and isolating the requirements of each component.
I want to be able to test components going forward, but I'm at a stage in development where each component depends on the complete output of others to be fully testable.

I can spoof the ideal output for one component and plug that in while the true component is incomplete; however, this requires a lot of thinking about the organization the project depends on.
A lot of those details are unresolved, and remain difficult to resolve. The problem, I think, is a tangle of perceived unresolved dependencies. Since nothing feels solidly defined, and since everything depends on something else, it's hard to pick a problem to tackle and fully define.

The school assignments I need to finish are:

- This journal (2450)
- Notes and AI Chat (2810)
- Questions 3 (3005)

Questions 3 should be done, I just need to submit the github link.
I'm annoyed with the notes requirement in 2810, but I think I took some decent enough notes, so it should be okay.

I have a few aspirational projects on my mind. These are things I'd like to start when I have nothing on my plate. Several of them came from brainstorming sessions with my team in this Software Engineering class.
- Webpage social media site, where each post by a user is a 500x500px view into a custom website. A social media site oriented toward technical users, where creativity and interactivity are the blood of posts.
- A dating app for CS students at Utah Tech... Codegrindr
- An AI bytecode-like instruction format designed to dispatch tasks to AI in atomic ways, leaving no complete task to a single agent that wouldn't be capable of an accurate answer.
- An NES emulator
- A simple server that monitors all my email accounts and pushes new emails to a small screen in my room.

# Mon Sep 22
## Journal 2

Professor Compas reminded me that I should be writing in my journal!

I'm going to go over Personal projects, School assignments, and Aspirational projects again. I want to make this a per-entry routine.

Right now, my largest personal project is still that Scratch VM. I got past the biggest hurdles in design and architecture, and it's solid right now. However, I'm up against some pretty frustrating bugs and the deadline is approaching. I need to have it done by the 13th next month or else I will have some issues. I do have time for this, though, especially with the break coming up.

My current school assignments are: 

- PPM menu (3005)
- Notes and AI Chat (2810)
- Project Pitch (2450)

I went ahead and did the main assignments in 2810, so I only have the weekly notes submissions in that class. My homework load is really quite light this semester. In Spring, I should be able to take on a whole lot of CS classes, especially since I won't have a big project to worry about.

I don't have any new aspirational projects right now.

# Fri Oct 3
## Journal 3

My main personal project is still the Scratch VM. I didn't work on it a whole lot between the 22nd and now. I did finally squash one of those tricky bugs, though, and I'm not incredibly worried about it. Worst case scenario, I do have a while after the technical deadline to make it better. Getting one of those bugs out of the way also helped me to feel more confident about going forward.

It's worth noting how strongly relevant and relatable Professor Compas' lectures on Software Engineering practices are to this project. It's almost like I make a mistake in the development process of this project, and the next week we talk about that exact mistake. Estimating timelines, defining issues and allocating timeframes/developer bandwidth, and creating efficient management systems are all obvious problems, but they don't have obvious solutions. I feel like as I bump into them on my project and then come up with my own solutions, I arrive pretty close to what Professor Compas talks about in class. But the lectures are incredibly helpful because they reinforce, clarify, and refine the solutions I come up with. And of course, it's often enough that I had no solution at all and the lectures provide one.

My current school assignments are:

- Notes and AI Chat (2810)
- This Journal (2450)

I'm still frustrated by that AI chat assignment. Russ stopped requiring the submission of notes, and so I stopped taking them. I've started just recalling and summarizing lectures instead.
I also went ahead a few weeks in 3005, so that's taken care of for the time being. I've been slacking on the journal, though! I'll try to make an entry tomorrow or before I submit on the 5th.

I have some very cool new aspirational projects:

- A universal interactive app API that identifies matchable system specs and deploys the highest-performance API it can given the specs. Any system, no matter how strange, should be capable of streaming media data through stdin/stdout. This is low performance, but is fine as the worst possible fallback. The API will be written from a minimal form up for each system. Every app written with this API should work anywhere, but dedicated implementers can write a version of the API that takes advantage of hardware accelerations. I wrote a document about this that I'll put in this commit.
- Extending the Image editor implementation we're making in 3005 to be a featured command line tool that feels as ergonomic and feature-complete as an industry standard. I would implement vimlike motions, cursor state, image edge/contour detection, advanced visual filters, bezier curve rendering, arbitrary polygon drawing, and text rendering.
- A rehash of my old C json parser that I wrote before I had a really strong handle on C. It would be very interesting to see how far I've come.
- A modified python version that optimizes it for bashlike ergonomics, and then a terminal emulator that uses this as the interpreter.
- A buffered SSH client bundled with a neovim extension that writes files remotely via scp, so remote development can be done with minimal latency. Top level bash prompt is interpreted, using buffers and interceptions to allow a seamless low-latency experience. stdin would be buffered when the client reasons that the host is interacting with a bash prompt (looks for a sentinel prompt). Malicious programs could easily fool it, but there would be little reason to. `vi`, `vim`, `nvim`, will be intercepted, and the user will instead be put into a local neovim instance that syncs reads and writes with the remote file being edited. The syncs would be done asynchronously, so the only latency across the system would be waiting for commands to return input.

This might be best as a client-first passive-server model. Instead of the client maintaining a persistent connection with remote, it would cache a local virtual filesystem representing remote. Reads and writes would happen over scp, and as long as a file is being actively edited, syncs would happen frequently. That the client machine is the stage for changes would be made clear. Instead of being "travel to the remote server and make changes there", it would be "use this facade to modify the filesystem locally in a way that immediately syncs with remote." There would be a channel for running commands on remote, and it would ideally be convenient and ergonomic, but the idea would be oriented toward simple file editing, using the resources available on the client's filesystem.

# Sat Oct 4
## Journal entry 4

Since yesterday, my assignments and personal projects haven't changed.

Personal Project: Scratch VM

School assignments: This journal, Notes and AI Chat

A new aspirational project I imagined is a unique fixed-length text encoding that's essentially indexed text. Strings would be passed around along with a short header of unicode or unicode-like code points, and each character in the string that exceeds the ascii range (>128) would represent an index into this table. The header would also allow strings to specify 16-bit characters, allowing an essentially inexhaustible set of indices to specify. String operations would be more complex, as they would have to maintain this table, but it would be doable and enable a majority of english strings to be encoded with fixed-length characters. utf-8 allows several-byte characters, meaning indexing a string at n isn't guaranteed to give you the nth printable character.

An interesting idea I had is that every data format sits on a spectrum from a hardware compatible buffer to a turing-complete interpreted language. Some data formats are very simple and essentially represent the exact values you would bit-bang onto the pins of a hardware device. Other data formats are the input to a turing-complete virtual machine. Most data formats sit somewhere on this spectrum, not cleanly on either side. The fundamental core of this idea is that all data are used to change what a computer will do. It's not a question of *whether* one piece of data in a stream will change how the computer will interpret other incoming data (A defensible definition of "code"), it's a question of *how much*. Code is essentially data folding back on itself, and the nature of all data is to what degree this happens.

TTF is a good demonstration of this principle. The font format is actually a set of instructions for a glyph-drawing virtual machine, and it has been a surface for exploits and viruses before.

This brings up a fundamental issue of sandboxing software. We can obviously see why sandboxing is important when we code a virtual machine that has access to system components. If we arbitrarily respect the intentions of all incoming data, malicious actors can cause serious issues. When we model all data as code by saying something like "all data must fundamentally have an effect on the running state of a program, or else it is not data.", then we can see the issue: interpreting all data is a matter of trust, and it's very easy to develop a system where input data has more power than you anticipated. Arbitrary Code Execution doesn't have to mean you're compiling users' data into rwx memory and then executing it. It can also mean that the nature of your format enables exploits via intended paths.

## Bare Metal

A quick extra entry today. No project overview because they haven't changed since earlier.

It's funny how hard it really is to actually program on bare metal.

When I started learning programming in python, I noticed there was a lot of code I wasn't writing. my question was "how do I do what these functions do, without using them? How do I accomplish this by myself?

The answer was to look at a lower-level language like C, where all of the functions are implemented in that language. I realized that even in C, there were plenty of functions that I wasn't writing.

So I learned assembly, and about how we use syscalls to accomplish common tasks - which are functions I didn't write,

So finally I look into OS-less programming, where everything is up to you...

Except, of course, the functions provided by a table in the firmware, which I didn't write.

We stand on the shoulders of giants.

# Sun Oct 5
## Rat idea

We don't like rats in our homes. But why? Personally, if it wasn't for a few risks and damages, I'd love to know there's some little guys scurrying in my walls. I certainly hate the idea of killing them with traps.

Rats chew on wires, leave droppings, and potentially spread disease. What if there were rats trained/bred to avoid these behaviors, including a little rat litter box, and to outcompete any untrained ones? Knowing rats are pretty smart, I suspect you could train them to avoid chewing wires and walls, and to leave droppings in a specific box. Rats from a lab are less likely to spread disease than rats from the outdoors.

There's no way to make it practical I don't think, but I bet it's very possible for a lab to train and breed these domestic rats for homes so that wild rats don't infiltrate. If I had 1 billion dollars to spare, I would found this company.

I have similar ideas for ants. If you can't beat em, breed and train versions of them that do your bidding and outcompete wild ones.

# Mon Oct 6
## Notes and AI Chat 2810

Man, these assignments are just oppressive. I am not remotely a note taker, and I retain information just fine by paying attention in the lectures. I'm ahead weeks in assignments, I've scored full points on all the quizzes bar one where I missed one point, and I can summarize a week's lectures just fine. I understand that note taking is theoretically a good habit and it helps with retention, but I don't struggle with retention.

All that would be fine if the assignments were <10% of my grade. If I could get a B without doing them assuming I got 100% on everything else, I think that would be fair game. But they're worth 25%! I can't get better than a C without doing them.

## A slight gripe

I don't like when people describe things as being true "becuase of x's theorem" or similar. Nothing is true "because a scientist discovered it". A sufficient definition of the first principles of the universe necessarily also describes every true theorem. That definition is likely pretty brief. I guess my gripe is that theorems are a description of the truth, not the principles behind it. When people cite a theorem, they're really just saying "my proof that x is true depends on the research of y and their theorem", but they generally phrase it such that the theorem *is* the principle that makes x true rather than a description of a logical consequence of the universal principles that make x true.

# Wed Oct 8
## Funny Coincidences

I haven't done a project indexing entry in a minute, so I'll do that quickly, although not much has changed.

My personal project is still the Scratch VM. I have 5 more days to work on it, and although I'm nervous, it's going well. My meeting with Jeff yesterday was really helpful; if nothing else, then for his pep talk.

I have no school assignments to do right now, which is a relief. I'm ahead in everything, though if I get too comfortable, I'll fall behind. I'm only a week ahead in 3005, and I'm only "ahead" in 2450 in that I'm caught up to this week a few days before I need to be. 2810 is fine, though, since I'm caught up to December in that class.

No new aspirational projects, or at least nothing I've cared enough to remember.

It's very funny to me how applicable this semester has been to the development of my Scratch VM. Between the fact that every week in Software Engineering feels like an eerie retelling of the mistakes I've made on this project, how 3005's assignments are very similar to my implementation of image processing, and how 2810 deals with the mechanics of the type of machine I'm emulating with my scratch machine, the classes I picked for this semester feel tailored to guide me through this project.

# Sat Oct 11
## Manual Memory Allocation safety technique

I had an idea for a memory allocation technique that could potentially ease a lot of the difficulties of manual management in low level code. If each allocation is owned by a stack frame and associated with that frame pointer, You can easily iterate over allocated blocks and tell which ones need to be freed by comparing against the current frame pointer. Very few allocations need to be done such that they *cannot* be linked to a stack frame, and those ones that do can default to typical memory allocation patterns.

# Sun Oct 12
## ESP Binary Patcher

The ESP32 has a tool that can use webUSB to flash prepared executables via web browsers. The issue is that the executable must exist; There are currently no web tools of which I am aware for compiling ESP32 natively in-browser. These shouldn't really be that difficult to create via webAssembly ports, but I have an idea for a different solution. Probably not a better one, although it could potentially be more lightweight and might be better in some cases. The tool would take in specially prepared binaries, where they have been compiled with custom section data. This should allow the tool to read that section of the prepared elf and customize inner data. The tool would use a map to find and modify variables, and possibly even functions. Rather than compiling complete C or C++, it would compile a highly reduced scripting format. This would use very simple machine instructions, make no attempt at optimization, and it would not be intended for any amount of heavy lifting. It would essentially be a glue between the functions that are already defined, and way to dispatch them dynamically in a way that just variable editing can't do ergonomically. This would allow people to publish their scripts in a flashable format, while still allowing some customization and option editing.

# Sun Oct 19
## SaaS and perspective on software

I see lots of people posting online about Software as a Service, and the whole thing looks like a clown show to me. It looks like seminar after seminar of people shaking each others' hands about low-hanging ideas and coming up with cool new abbreviations and making up rules for what good software is and how to get hired. It's all so self-congratulatory, and I don't feel that I have evidence of its actual function. I think it's a particular mindset that irks me. Some people seem to go around the world seeing new things and thinking, "how can I use this? How can I turn this into new work for myself so I can engage in a superficial grind?", and that worldview is just incredibly poisonous to me. These people write linkedin posts about how "weddings are a great place to network", and I just don't buy it. The core of the issue, I think, is that these people refuse to acknowledge there are some types of lightning you just can't put into a bottle. Some things just get way worse when you try to cultivate them and capture what makes them good. Networking is great, and weddings might be a good place to do it! But the phenomenon these tech bros have tech-ified into "networking" is just Making Friends! How obvious is it that making friends is a productive thing to do? Tech bros drain the play out of things, try to make them efficient, and don't see how they've made something that was dead from the start. It's the same reason dating apps are terrible. Some tech bro probably saw an instance of people meeting on the internet and building a happy relationship and thought to himself, "how do I capture that in a bottle?" It's not necessarily a bad idea. But by trying to make that phenomenon reproducible and scalable, that tech bro lost sight of the play and freedom that made the original interaction successful in the first place. 

A related gripe is a semi-belief I hold; something I don't quite rationally think is true, but a belief I find myself gravitating toward when I'm not paying attention. I tend to think that the rule is "Software is for games, curiosity, and exploration", and that's why I love it. I tend to imagine that any actual use for software is the exception to the rule, and while I'm glad it exists for the sake of my employment, I don't totally respect it. Software is foremost fun and intellectual, and useful by coincidence.

# Tue Oct 21
## Project Update

I still want to make project update journal entries a regular thing, I just haven't had new updates recently.

My assignments are pretty standard: Some 3005, some 2450, and some 2810. I didn't do the last Notes and AI chat, but I'll get the next one. Annoying how much it affects my grade. I'm running into a bit of Tortoise And The Hare with 3005, as I'm sincerely behind on an assignment for the first time in the semester. I submitted one late, but by 30 minutes. This is the first time I've actually had no progress on the assignment a day after it was due. The penalties are kind in this class, though, and I need to focus on polishing the scratch project for the time being. Professor Compas is understanding, and I think he may give me even more lenience because of how cool the scratch project is.

My personal project continues to be the scratch project. I had it in the minimum viable state by the due date on the 13th, but it's still far from perfect and needs hours more of my attention.

I'm writing this entry because I came up with the coolest aspirational project ever.

I recently bought a vintage typewriter because I think the technology is cool. My idea is to hook up a reading mechanism to it (so that keypresses can be registered electronically) and a writing mechanism to it (so that a computer inside can pull levers and type on it automatically) and turn it into an analog unix terminal. I think I would be able to die happy if I had that machine in my room. What a cool idea.

Imagine if I could hook it up to an LLM and have a haunted typewriter! I will try to do this over the Christmas Break.

# Sat Nov 1
## AI jobs

I have felt a particular way about AI and its ability to take programmer jobs for a while, but I just now found the words to express it.

The heart of the matter is that I have found no sincere proof that current AI agents, including any permutation of checked-balanced system, with any number of agentic peers, can do jobs more complicated than data entry.

A *lot* of modern "programming" jobs are just barely different from entering data into excel spreadsheets. It's the same basic deal, with a different interface and slightly more complexity in the form of debugging.

Almost all app/web design falls under this umbrella. Putting together html and CSS into a webpage is certainly under it. Hacking together a backend and a schema that uses no innovative technology is data entry. Using javascript to coordinate frontend state transfer is data entry. Maintaining an old system is data entry. A *lot* of programming jobs can and should be cut by AI, because they were essentially manual excel spreadsheet management to begin with.

Real system design requires more context than agents have, at least for now. Checked-and-balanced models with access to running their code can get there eventually, but their low context window means all they can do is focus on one issue until it stops happening. Certain features lay across valleys of "irreducible complexity" where iterative, focused bug fixes cannot lead there.


# Mon Nov 3
## Minecraft Redstone

I had a very odd start to my computer science journey. I started in Minecraft, where the in-game command system enables some pretty neat turing-complete behavior. I learned and experimented with that system for a very long time before I ever touched a formal programming language.

It led me to explore the ingame logic system, which is not locked behind console commands, redstone.

Redstone is a system which allows you to create, propagate, read, invert, and subtract logical levels enumerated from 0 to 15, inclusive, via a survival mode accessible set of blocktypes. It is fully turing complete, and with all components (or even a highly restricted subset), you can create any configuration of logic and state, and indeed complete computers.

I was taught the basics of binary code some time along the line, and I intuited much of the rest. I looked up how to make an adder with redstone, but I didn't understand it. It was a somewhat optimized version, and it was based on logic gate configuration tables. Instead of learning to understand that directly, I sat on my knowledge of binary code until I figured out addition on my own.

I intuited subtraction and two's complement, realizing that it generalized to any base.

I had built a decimal addition calculator before I learnt python. It used a stateful clock system, where a 10-state clock was paused until given an input, how long to unpause for. Each loop, it would propagate a 1-tick unpause signal up. The clock would write to a 7-segment display, with each node corresponding to a different glyph on the display.

I had built a typewriter, where binary strings enumerated glyphs via a decoder, around the time I was introduced to programming languages. At that time, I realized I had been scared of formal programming languages for no reason. Python came naturally to me, and after plenty of discovery, I settled into an acceptable coding style. I wrote plenty of garbage code that I thought was innovative and proper at the time, heavily abusing python's introspective type system.

After that, I coasted with Python for a while, writing a few neat games and other program types. I ignored my assignments and got bad grades, but I learnt a lot.

An itch still had to be scratched, though. I remembered my redstone days where I was touching bits directly. I knew that was the basic reality of computer science, but where was it? In python, it's almost nowhere to be found. Where does the print function come from? How do graphics applications draw to the screen? Where does all this complexity come from? I was frustrated, because I could not see the feet of the shoulders I stood on.

This got me curious about C programming, which I heard was the low-level fix I craved. I learnt the basic syntax, and I admired it, but it was too foreign from the python I was familiar with and I shelved it temporarily.

I took a foray into web programming with Code School, a summer program offered by Utah Tech. I learnt javascript, built on some rudimentary html/css I had picked up from a prior class, and designed a cruddy little app. I was still a concurrent enrollment high schooler, and I teamed up with another high schooler even a year younger than myself, so we weren't expected to make anything great. Still, I learnt a lot and haven't forgotten it.

I still had that itch. Learning javascript gave me some awesome ideas. It's really quite a cool language, despite its terrible quirks. Its closure state system is as cool as it is confusing. The ubiuqitous object syntax is very interesting. I took lessons from javascript and made a naive programming language specification. I had some cool ideas, but was ultimately out of touch with what a programming language can and can't do.

Above, I suggested that I only dipped my toes into C, but I was actually pretty confident in my ability at the time. A bit of Dunning-Kruger for you. C can be deceptive that way, making you think you know the language before you really do. I had learned how to do the basic things, but if I were to write a C program, I would've still written it like python and gotten frustrated when python patterns were so heavy and full of friction. It wouldn't be until the following fall that I gained a deep understanding of the language.

Learning C is really learning all the terrible things you can do with it and why you shouldn't do them. If you don't know 1000 different ways to cause a segfault, and if you just see a segfault as a unary despair, you aren't intimate with C. 

The fall after code school, I took an internship across the states in Maryland. I spent my 9-5 hours as a daycare employee on a Navy base, keeping Navy kids fed, happy, and safe. I couldn't take any classes for my degree online, so I had little to do in my free hours. I made a habit of walking long distances, and that was very enriching, but I also rehashed my interest in C. This is where I really earned the right to say I knew it. I made a little asteroids game, introduced myself to SDL, banged my head against countless segfaults before I learned gdb, and actually began to look into assembly.

My interest in assembly had been piqued before, but it always seemed far away. I only learned it really in passing, via C inline assembly. Inlining assembly in C is actually a pretty good crutch for learning it, although the syntax is dense. With a proper preprocessor allowing less obtuse assembly syntax, I would recommend it as a teaching method.

I learnt some intel assembly, along with some ARM. I remember slaving over a C program that allocated some executable memory, wrote the machine code for some ARM instructions into it via binary literals, cast it to a function, and called it. That was pretty seriously cool.

I picked up interest in rust, checked out a book on it from the library in Maryland, and decided it wasn't for me. Too bureaucratic for my tastes, though I do respect it in principle.

Since that time, my growth has been pretty linear. At the end of that internship, I still wasn't a C expert by any means, but I consider myself something of a wizard in it almost a year later. I know it well enough to understand where it suffers from old design choices and I can actually reason about how to replace them with pragmatic, zero-cost syntax. I've written a low-level language doc that's essentially a revision on top of C and takes some decent inspiration from the naive one I wrote before. I've come very far from my humble beginnings, and I mainly have redstone to thank for my journey.

I'd love to return to it soon, maybe make a full computer and write some programs for it. I've got some good ideas. Maybe when I have some more time.

# Tue Nov 4
## Four project ideas

I have something important to work on, so I've got to jot these ideas down really quickly.

- Command line argument parsing library. These exist, but I've got a good idea for one.
- `Gitfriend`, a bot that watches what you do in a repository and helps with things like merges, commit messages, project status, issue management, etc. Lets you ask things like, "where is the function `printLogs`? and has a way to dispatch deterministic methods for answering questions, such as `grep`.
- `Refactor`, a tokenizer-chatbot duo that lets you run coordinated, deterministic refactoring functions. database-like syntax, perhaps `refactor main.c for function "check function for correctness."` would prompt a new agent session to check each function for correctness individually. `refactor main.c for function "implement function if not implemented." Would let the chatbot do a global pass to collect necessary context.
- A command line chat application where you only have two streams: an anonymous outgoing message queue, and an anonymous incoming message queue. When you send a message out, the algorithm determines which users would probably like to see your message. When you check your inbox, you can reply to users, but you can only either reply to the top message or discard it. You cannot see your full inbox at once. If you receive a reply in your inbox, the full context of the chat is included.
