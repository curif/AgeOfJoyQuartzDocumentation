The emission file mask is an image that [[AGE of joy]] uses to create a lighting effect in a cabinet part.

[[CDL the Cabinet Description Language]] example:

```yaml file="description.yaml"
- name: joystick
    art:
      file: joystick.png
      inverty: true
      invertx: true
    emission:
      emissive: true
      color:
        r: 255
        g: 255
        b: 255
      art:
        file: joystick_emission.png
        inverty: true
        invertx: true
```

| ![[Pasted image 20240306120500.png]] | ![[Pasted image 20240306120519.png]] | ![[Pasted image 20240306120701.png]] |
| ------------------------------------ | ------------------------------------ | ------------------------------------ |
| `joystick.png`                       | `joystick_emission.png`              | final result                         |
> ![note]
> You can turn on / off the emission and change the emission color using [[AGEBasic programing]]

