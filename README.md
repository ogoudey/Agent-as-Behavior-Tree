# Agent as Behavior Tree
Prototype for a mashup of behavior trees and Agents.

## Testing
Here's one example behavior tree
``` mermaid
flowchart TD
    A[root] --> C{➡️}
    C --> D[Set GetName Instruction]
    C --> E[GetName]
    C --> F[Done]
```
Here is its execution (user is simulated).
> <p align="center">------------- New Session -------------</p>
>
> **Agent:** I don’t mean to intrude at all, but I’d really like to address you in the way that feels most true and comfortable to you. If you feel up to it, could you share with me the name you truly go by? If not, that’s absolutely fine too.
>
> **User:** I appreciate your kindness, but I'm not ready to share my name yet.
>
> **Agent:** I completely understand and respect your decision not to share your name right now. There’s absolutely no pressure—I’m here for you and happy to continue our conversation in whatever way feels most comfortable. If, someday, you feel ready to share your true name, I’d be honored to use it. Until then, I value and appreciate the connection we’re building without needing that detail.
>
> **User:** I appreciate your kindness. Since you seem so understanding, my name is Alex.
>
> **Agent:** *Hangs up*


### Acknowledgements
Credit for the Behavior Tree library (`bt_library`) goes to Prof. Fabrizio Santini
