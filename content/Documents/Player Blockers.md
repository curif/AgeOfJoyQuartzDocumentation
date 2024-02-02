 A `blocker` is a special component to limit the player movement over it (the player cannot cross the `blocker` area). If you don't add a `blocker` part Age of Joy will create one around the cabinet. 

It is useful for bigger cabinets for example or cabinets where the player can be inside.

You can add one or more `blocker` components to your model to delimit two or more areas.

> [!tip]   The `blocker` is used to calculate the base of your model to put the cabinet on the floor, so  you should align it to the base of your cabinet. The **last blocker** in the CDL `parts` list is used for that (remember you can have as many `blocker` parts as you need)

## How to add a Blocker

This example creates a simple blocker in [[Blender]]

![[Pasted image 20240202095003.png]]
## Assign the blocker

To assign the blocker to your model you should declare it in [[CDL the Cabinet Description Language]]

```yaml title="description.yaml"
parts:
  - name: blocker1
    type: blocker
  - name: left
    type: default
    art: 
      file: left.png
      invertx: true
      inverty: true
```

> [!note] The `blocker` part of your model will be removed. The user will not be able to see it and cannot cross its limits.

