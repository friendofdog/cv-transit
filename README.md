Covid Risk Assessment – Transit Seating
=======================================

A calculator to assess risk-over-time of exposure to covid on public transit.

This application takes a single row of seating on a train and assesses the risk of exposure to covid based on proximity to other commuters over the lenght of time each person is expected to remain seated. Underlying assumptions are:

- A row consists of a number of seats. The row is a straight line and seats are adjacent to each other without a gap or divider.
- A commuter will spend a given amount of time on the train. This time is arbitrary and, for simplicity's sake, is the same for all commuters.
- As commuters embark, they take a seat if one is available. If all seats are occupied, commuters stand until a seat is available. While standing, a commuter is merely "on hold" and is not a factor until he sits down.
- Commuters sit on a FIFO basis. Commuters who have been waiting longer for a seat sit down first. Seats will be occupied in reverse order of their risk level (low-to-high).
- Commuters can be wearing masks or not. Those not wearing masks increase the risk by 70% (based on several Internet memes which state that masks reduce transmission risk by 70%).

Models
------

### Seat

A seat consists of three attributes:

- position: the position of a seat, from the left, starting at 0 and ending with n-1
- threat: the risk that a seat poses to adjacent seats, based on the time a commuter has remaining and whether or not he's wearing a mask
- exposure: a seat's exposure to risk, based on adjacent seats' threat level

### Commuter

A commuter consists of two attributes:

- time: the amount of time remaining that a commuter will be on the train
- mask: `True` or `False`, depending on whether he's wearing a mask

### Row

- occupancy: the individual seats which make up a row
