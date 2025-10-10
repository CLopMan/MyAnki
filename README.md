# My Anki

MyAnki is a personal project to develop a light app to study for exams through flashcards. It is not created to substitude [Anki](https://apps.ankiweb.net/), but to practice my python skills and achieving something helpful that I could use. Obviously, it is strongly inspired by the preovious mentioned app.

## Technologies used
- Python 3.13: as the main Programming Language in which is written the business logic
- PyQT: to build the HMI
- Pydantic: in order to load data and validate JSON-based structures

## Main architecture
```mermaid
    flowchart LR
    json@{ shape: docs, label: "decks stored as json"} <-->|Adapter| D(Data object)
    D <--> G[\GUI\]
```
