
> [!warning] Available in [[Age of Joy]] v0.6 or superior.


Cabinet parts typically represent static or decorative objects that do not interact with the player or the environment. However, certain parts may need to respond to environmental factors, such as gravity or player interaction. In these cases, the part should be defined as `physical`.

**Example:**

```yaml
  - name: wall1
    physical: 
      shape: box
      receive-impacts:
        parts: 
          - sphere
          - sphere.001
          - sphere.002
        repulsion:
          force: 1.5
```

In this example, if any of the listed parts (e.g., `sphere`, `sphere.001`, `sphere.002`) collide with the wall, they will be repelled with 50% more force than usual.

### `physical` Properties

- **`physical`**: Indicates that the part can interact with the player and the environment.
  - **`shape`**: Defines the approximate shape of the part. The default is `box`, but you can choose another option like `sphere` for round objects or `capsule` for objects shaped like a person.
  - **`receive-impacts`**: Specifies which parts can collide with this part (e.g., a ball).
    - **`parts`**: A list of cabinet parts that can interact with this part. Collisions from other parts that aren't in the list are ignored.
    - **`repulsion`**: If set, the part will repel any colliding objects with the specified force.
      - **`force`**: Defines the strength of the repulsion. The default value is `1`, which can be adjusted to increase or decrease the force applied when a collision occurs.



## Physical Material

(From the Unity's manual)

The physical material defines the characteristics of the part, such as whether it is heavy, hard, or made from something like rubber. For example, the following YAML defines a rubber material for a part, that is spherical, and is affected by the world gravity.

```yaml
  - name: sphere.001
    physical:
      shape: sphere
      gravity: true
      material:
        dynamic-friction: 0.6
        static-friction: 0.6
        bounciness: 0.8
        friction-combine: average
        bounce-combine: maximum
```

- **`gravity`**: Determines if the part is affected by the 3D world's gravity. The default is `false`, but setting it to `true` will make the part behave according to gravity. For example, when a player inserts a coin, the part may fall and bounce off other cabinet parts, the floor, or other objects. If you plan to control the part using [[AGEBasic]] don't set it as `true`.
- **`material`**: Specifies the physical material that the part is made of.

### Material Property

The following properties define how the part behaves when interacting with other parts, based on Unity's physics system:

| **Property**           | **Description**                                                                                                                                                                                                                                         |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`dynamic-friction`** | Defines the friction between moving surfaces. The value ranges from 0 (no friction, like ice) to 1 (high friction, like rubber). The default is 0.6. Unity calculates friction based on the `friction-combine` property.                                |
| **`static-friction`**  | Defines the friction between surfaces when they are stationary. The value ranges from 0 (no friction) to 1 (high friction). The default is 0.6. Unity calculates static friction based on the `friction-combine` property.                              |
| **`bounciness`**       | Determines how much the part bounces. A value of 0 means no bounce (like clay), while 1 represents full bounce (like rubber). The default is 0.0. The physics system uses this value with the `bounce-combine` property to determine the bounce effect. |
| **`friction-combine`** | Controls how friction is calculated when two parts touch. Options include: `maximum`, `minimum`, `multiply`, or `average`. The default is `average`.                                                                                                    |
| **`bounce-combine`**   | Controls how the bounce is calculated between two parts, based on their `bounciness`. Options include: `maximum`, `minimum`, `multiply`, or `average`. The default is `maximum`.                                                                        |

#### How Collider Surface Values Combine

When two physical parts come into contact, the system uses the `friction-combine` and `bounce-combine` properties to calculate total friction and bounce. The available options are:

|**Priority**|**Property**|**Description**|
|------------|------------|---------------|
|1           |**Maximum**  | Uses the largest value between the two parts.|
|2           |**Multiply** | Multiplies the two values together.|
|3           |**Minimum**  | Uses the smallest value between the two parts.|
|4           |**Average**  | Uses the average of the two values.|

These options provide flexibility in determining how parts will interact when they collide.
Here's a refined version of the "Player Interaction" section:

---

## Player Interaction

Cabinet Artists can design their cabinets to respond to player interactions, such as touching or grabbing parts.

**Example:**

```yaml
- name: wall2
    physical: 
      player-interaction:
        can-touch: true
        can-grab: false
```

- **`physical`**: Indicates that the part can interact with the player and the environment.
  - **`player-interaction`**: Defines the types of player interactions allowed.
    - **`can-touch`**: The default is `false`. Setting this to `true` allows [[Age of Joy]] to detect when the player touches the part with their hands (while the game is running).
    - **`can-grab`**: _Not available yet._

## AGEBasic event system

To complete the cabinet functionality [[Cabinet Artist]]s should use the [[AGEBasic event system]] (available on version 0.6 and superior).

Using [[AGEBasic event system]] is possible to program [[AGEBasic]] scripts to react to physics and interactions. It is possible to execute code when a part touch another or when the player touch a cabinet part (for example). 