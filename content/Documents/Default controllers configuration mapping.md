
[[Age of Joy]] has an internal mapping configuration that aligns with commonly used controllers available in the market. This means that when you connect your controller to the headset, there is a high likelihood that it will work without any additional setup or configuration.

### The default mapping table


| MAME | Control | Behavior | Port | Unity Path |
| ---- | ---- | ---- | ---- | ---- |
| JOYPAD_B | quest-b | 0 | button | `<XRController>{RightHand}/secondaryButton` |
| JOYPAD_B | gamepad-b | 0 | button | `<Gamepad>/buttonEast` |
| JOYPAD_B | quest-right-trigger | 0 | button | `<OculusTouchController>{RightHand}/triggerPressed` |
| JOYPAD_B | keyboard-enter | 0 | button | `<keyboard>/enter` |
| JOYPAD_A | gamepad-a | 0 | button | `<Gamepad>/buttonSouth` |
| JOYPAD_A | quest-a | 0 | button | `<XRController>{RightHand}/primaryButton` |
| JOYPAD_X | gamepad-x | 0 | button | `<Gamepad>/buttonWest` |
| JOYPAD_X | quest-x | 0 | button | `<XRController>{LeftHand}/primaryButton` |
| JOYPAD_Y | gamepad-y | 0 | button | `<Gamepad>/buttonNorth` |
| JOYPAD_Y | quest-y | 0 | button | `<XRController>{LeftHand}/secondaryButton` |
| JOYPAD_START | gamepad-start | 0 | button | `<Gamepad>/start` |
| JOYPAD_START | quest-start | 0 | button | `<OculusTouchController>/start` |
| JOYPAD_SELECT | gamepad-select | 0 | button | `<Gamepad>/select` |
| JOYPAD_SELECT | quest-select | 0 | button | `<XRController>{RightHand}/menuButton` |
| JOYPAD_UP | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| JOYPAD_UP | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| JOYPAD_DOWN | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| JOYPAD_DOWN | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| JOYPAD_LEFT | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| JOYPAD_LEFT | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| JOYPAD_RIGHT | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| JOYPAD_RIGHT | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| JOYPAD_UP | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| JOYPAD_UP | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| JOYPAD_DOWN | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| JOYPAD_DOWN | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| JOYPAD_LEFT | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| JOYPAD_LEFT | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| JOYPAD_RIGHT | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| JOYPAD_RIGHT | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| JOYPAD_L | quest-left-trigger | 0 | button | `<OculusTouchController>{LeftHand}/triggerPressed` |
| JOYPAD_L | gamepad-left-trigger | 0 | button | `<Gamepad>/leftTrigger` |
| JOYPAD_R | quest-right-trigger | 0 | button | `<OculusTouchController>{RightHand}/triggerPressed` |
| JOYPAD_R | gamepad-right-trigger | 0 | button | `<Gamepad>/rightTrigger` |
| JOYPAD_L2 | quest-left-grip | 0 | button | `<XRController>{LeftHand}/gripButton` |
| JOYPAD_L2 | gamepad-left-bumper | 0 | button | `<Gamepad>/leftShoulder` |
| JOYPAD_R2 | quest-right-grip | 0 | button | `<XRController>{RightHand}/gripButton` |
| JOYPAD_R2 | gamepad-right-bumper | 0 | button | `<Gamepad>/rightShoulder` |
| JOYPAD_R3 | quest-right-thumbstick-press | 0 | button | `<XRController>{RightHand}/thumbstickClicked` |
| JOYPAD_R3 | gamepad-right-thumbstick-press | 0 | button | `<Gamepad>/rightStickPress` |
| EXIT | quest-left-grip | 0 | button | `<XRController>{LeftHand}/gripButton` |
| EXIT | gamepad-left-bumper | 0 | button | `<Gamepad>/leftShoulder` |
| EXIT | keyboard-esc | 0 | button | `<keyboard>/escape` |
| INSERT | gamepad-select | 0 | button | `<Gamepad>/select` |
| MOUSE_X | quest-right-thumbstick | 0 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| MOUSE_X | gamepad-right-thumbstick | 0 | axis | `<Gamepad>/rightStick` |
| MOUSE_X | quest-x | 0 | axis | `<XRController>{LeftHand}/primaryButton` |
| MOUSE_Y | quest-right-thumbstick | 0 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| MOUSE_Y | gamepad-right-thumbstick | 0 | axis | `<Gamepad>/rightStick` |
| MOUSE_LEFT | quest-b | 0 | button | `<XRController>{RightHand}/secondaryButton` |
| MOUSE_LEFT | gamepad-b | 0 | button | `<Gamepad>/buttonEast` |
| MOUSE_RIGHT | quest-a | 0 | button | `<XRController>{RightHand}/primaryButton` |
| MOUSE_RIGHT | gamepad-a | 0 | button | `<Gamepad>/buttonSouth` |
| MOUSE_MIDDLE | quest-x | 0 | button | `<XRController>{LeftHand}/primaryButton` |
| MOUSE_MIDDLE | gamepad-x | 0 | button | `<Gamepad>/buttonWest` |
| MOUSE_WHEELUP | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| MOUSE_WHEELUP | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| MOUSE_WHEELDOWN | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| MOUSE_WHEELDOWN | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| MOUSE_HORIZ_WHEELUP | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| MOUSE_HORIZ_WHEELUP | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| MOUSE_HORIZ_WHEELDOWN | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| MOUSE_HORIZ_WHEELDOWN | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| MOUSE_BUTTON_4 | quest-left-thumbstick-press | 0 | button | `<XRController>{LeftHand}/thumbstickClicked` |
| MOUSE_BUTTON_4 | gamepad-left-thumbstick-press | 0 | button | `<Gamepad>/leftStickPress` |
| MOUSE_BUTTON_5 | quest-right-thumbstick-press | 0 | button | `<XRController>{RightHand}/thumbstickClicked` |
| MOUSE_BUTTON_5 | gamepad-right-thumbstick-press | 0 | button | `<Gamepad>/rightStickPress` |
| LIGHTGUN_AUX_A | quest-a | 0 | button | `<XRController>{RightHand}/primaryButton` |
| LIGHTGUN_AUX_A | gamepad-a | 0 | button | `<Gamepad>/buttonSouth` |
| LIGHTGUN_AUX_B | quest-b | 0 | button | `<XRController>{RightHand}/secondaryButton` |
| LIGHTGUN_AUX_B | gamepad-b | 0 | button | `<Gamepad>/buttonEast` |
| LIGHTGUN_AUX_B | quest-right-trigger | 0 | button | `<OculusTouchController>{RightHand}/triggerPressed` |
| LIGHTGUN_AUX_B | keyboard-enter | 0 | button | `<keyboard>/enter` |
| LIGHTGUN_AUX_C | gamepad-x | 0 | button | `<Gamepad>/buttonWest` |
| LIGHTGUN_AUX_C | quest-x | 0 | button | `<XRController>{LeftHand}/primaryButton` |
| LIGHTGUN_DPAD_UP | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_UP | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| LIGHTGUN_DPAD_DOWN | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_DOWN | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| LIGHTGUN_DPAD_LEFT | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_LEFT | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| LIGHTGUN_DPAD_RIGHT | quest-left-thumbstick | 0 | axis | `<XRController>{LeftHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_RIGHT | gamepad-left-thumbstick | 0 | axis | `<Gamepad>/leftStick` |
| LIGHTGUN_DPAD_UP | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_UP | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| LIGHTGUN_DPAD_DOWN | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_DOWN | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| LIGHTGUN_DPAD_LEFT | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_LEFT | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| LIGHTGUN_DPAD_RIGHT | quest-right-thumbstick | 1 | axis | `<XRController>{RightHand}/Primary2DAxis` |
| LIGHTGUN_DPAD_RIGHT | gamepad-right-thumbstick | 1 | axis | `<Gamepad>/rightStick` |
| LIGHTGUN_START | gamepad-start | 0 | button | `<Gamepad>/start` |
| LIGHTGUN_START | quest-start | 0 | button | `<OculusTouchController>/start` |
| LIGHTGUN_SELECT | gamepad-select | 0 | button | `<Gamepad>/select` |
| LIGHTGUN_SELECT | quest-select | 0 | button | `<XRController>{RightHand}/menuButton` |
| LIGHTGUN_TRIGGER | quest-right-trigger | 0 | button | `<OculusTouchController>{RightHand}/triggerPressed` |
| LIGHTGUN_TRIGGER | gamepad-right-trigger | 0 | button | `<Gamepad>/rightTrigger` |
| LIGHTGUN_RELOAD | gamepad-start | 0 | button | `<Gamepad>/start` |
| LIGHTGUN_RELOAD | quest-start | 0 | button | `<OculusTouchController>/start`<br> |
| JOYPAD_LEFT_RUMBLE<br> | quest-left-haptic-device |  |  |  |
| JOYPAD_RIGHT_RUMBLE | quest-right-haptic-device |  |  |  |


#v0_4 