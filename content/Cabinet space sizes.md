[[cabinet]]s space is the size of the cabinet measure in cabinet units.


> > [!warning] 
> The contents of this document applies to [[Age of Joy]] version 0.4-RC04 or superior.

## Cabinet units

A cabinet unit is a string who represent *width*, *large* and *height* of a cabinet (`WxHxL`)

The minimal unit is `1` and the maximum is `2`. The default is `1x1x2` (one width, one large and double height).

### Example: 

The `1x1x1` size represents a *Cabaret* size cabinet.

Cabaret cabinet (`1x1x1`)

## CDL

The [[CDL the Cabinet Description Language]] allows the `space` key to register the cabinets' size. Short of *Occupied Space*.

Example:

```yaml title="description.yaml"
year: 1982
author: curif
size: 2x2x2
```


> [!note]
`spaces` are limited to: "1x1x1", "1x1x2", "1x2x1", "1x2x2", "2x1x1", "2x1x2", "2x2x1", "2x2x2"

## How it works

When you enter for first time in a room, [[Age of Joy]] will assign cabinets from the [[Cabinets database storage]] in replacement of the *out of order cabinets* (the black ones with the Age Of Joy logo marquee). AOJ tries to find the best match cabinet in the database, because each position in a room is registered to accommodate a type of cabinet. For example if a space could accommodate a 2x2x2 cabinet AOJ will try to find an unassigned one with that size in the database, if there isn't one it will use a 1x2x1 or a 1x1x2 cabinet.
## Sizes

### 1x1x1

Is the minimal allowed space. A Cabaret cabinet type fits in this space.

![[Pasted image 20240219161453.png]]

### 1x1x2

The standard sized cabinet. 
![[Pasted image 20240219161257.png]]

### 1x2x2

Cockpit cabinets, large light guns cabinets.

![[Pasted image 20240219161626.png]]

### 2x1x1

![[Pasted image 20240219161935.png]]

Cocktail like cabinet where the user can put a drink for example.

Usually the [[Cabinet Artist]] set the space to `2x1x1` leaving some space free around the cabinet to fit the player.


