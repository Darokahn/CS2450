Degrading Universal Media Interchange is an API and I/O machine that enables simple single-window UI applications with zero minimum graphics API integration.

The idea of Degrading Universal Media Interchange as a protocol is to decouple simple applications from any sort of I/O library specific to their operating system or hardware, and allow complex applications to define fallback methods for I/O with degrading performance per specification miss.

The API, at the highest level of degradation, uses only stdin/stdout for I/O. Applications will send out streams of data representing multimedia, and they will accept streams of data representing input.

The basic format of the interface is `command, datatype, datatype parameters, data transformer, timestamp, data`.

Each interchange will begin with a byte specifying what the following bytes mean. 0 is a special value meaning "fully expanded interchange". 1 is a special value meaning "define an interchange header", `2` is a special value meaning "use the last interchange header", and `3` is a special value meaning "define a data transformer".

The format for a fully expanded interchange, including the leading signal byte, is:

`0, datatype, datatype parameters, data transformer, timestamp, data`

For an interchange header definition is:

`1, number, datatype, datatype parameters, data transformer, timestamp, data`

where number is none of the taken special values in the range of 0-255

For a use-last command:

`2, timestamp, data`

For any other command:

`number, timestamp, data`

where number is a previously defined interchange header from 0-255

The interface will be highly programmable, with an interchange specification. It will have:
- Option setting
- Image definition
- Pixel Processing Unit with sprite config and placement commands
- Audio definition
- Audio Processing Unit with timestamped playback commands
- Virtual GPU which will be capable of accelerating certain graphics operations, but will not have the full range of motion of GPUs, which would require hardware and OS specific APIs.

The data transformers hinted at above are layers written in an interpreted language that apply to the data in an interchange. The data expected by the interface is always the simplest form of that datatype: Think PPM for images and WAV for audio. Data transformers are a way to send it in a compressed encoding so that it can be interpreted by the DUMI machine into the correct final data. The format for data transformers hasn't been finalized, but it will be optimized so that the DUMI machine can interpret it as efficiently as possible. It can also be compiled into RWX memory, at the discretion of the DUMI implementation.

Data transformer code will also be specifiable via hyperlink, so that necessary translation layers can be fetched if they aren't locally owned.
Data transformers will need to specify how much data they can provide per call, so that the DUMI machine can treat them as generators if necessary. If they cannot be generalized as generators, they must specify that they offer an entire rendered buffer at once.

An implementation of the DUMI API requires, at minimum, that it is capable of sending properly formatted commands to stdout and recieving formatted commands from stdin. A DUMI machine should be written for every hardware set and architecture, but there should be a basic DUMI machine that can run pretty much anywhere.

DUMI API implementations may also specify what happens if they can match hardware/software specs and optimize for them, providing increased performance.

The benefit of the DUMI API is several-fold. First, I/O programs are recordable and replayable. If you tee the output between the DUMI machine and a file, you can replay the file into the DUMI machine at any time. Second, programs can fall back onto the lowest-specification version of the API if every aspect of their spec misses an optimized version of it. Programs can always run, even if performance is compromised.

DUMI API implementations should fall back to stdin/stdout only as plan Z. If nothing else is guaranteed, at the very least your app will *run*. Maybe not quickly enough, but at least debuggably.

For many apps, the lowest common denominator for performance will be perfectly fine. I would love DUMI applications to replace the web in some capacity.
