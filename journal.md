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
