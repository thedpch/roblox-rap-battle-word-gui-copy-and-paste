import tkinter as tk
from tkinter import messagebox, Scrollbar, Canvas, Frame

def copy_to_clipboard(line_index):
    global copied_lines
    if line_index not in copied_lines:
        copied_lines[line_index] = rap_lines[line_index].split()
    current_word = copied_lines[line_index].pop(0)
    root.clipboard_clear()
    root.clipboard_append(current_word)
    root.update()
    messagebox.showinfo("Copied", f"Text copied to clipboard: {current_word}")

root = tk.Tk()
root.title("Rap Lines")
root.geometry("800x600")

canvas = Canvas(root)
scrollbar = Scrollbar(root, orient="vertical", command=canvas.yview)
scrollable_frame = Frame(canvas)

scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

rap_lines = [
    "I got the flow that's colder than ice, spit fire twice, so precise, breaking the vice, yeah, I'm nice.",
    "On the grind, making moves, chasing dreams, it's my groove, never lose, I got the proof, watch me improve.",
    "Hustle hard, break the chains, rise above, feel no pain, in this game, I maintain, success is my domain.",
    "Future bright, vision clear, making waves, have no fear, stepping up, pioneer, hear me loud and clear.",
    "In the zone, no distractions, big plans, making actions, feel the passion, satisfaction, my life's a chain reaction.",
    "Eyes on the prize, I won't quit, every hit, making it, taking risks, I commit, watch my skills, they transmit.",
    "I'm a star, shining bright, in the dark, I ignite, set the bar, reach new heights, live my dreams, day and night.",
    "Overcome, stand tall, through it all, never fall, heed the call, break the wall, I got it all, standing proud.",
    "Innovate, elevate, create my fate, never late, dominate, demonstrate, my name's engraved on the slate.",
    "Chasing gold, dreams unfold, heart and soul, never cold, bold and old, stories told, my journey's paved with gold.",
    "Beat the odds, rise above, self-love, hand in glove, fit like a dove, stay in love, my life's a treasure trove.",
    "Seek the peak, never weak, speak unique, life's mystique, tweak the technique, my dreams are never oblique.",
    "Spitting bars, sharp as knives, you talking trash, living lies, I'm on the rise, no surprise, your career's in a nosedive.",
    "My flow's so tight, it could squeeze you out, your rhymes so weak, they got no clout, step to me, without a doubt, I'll roast you up and spit you out.",
    "I'm the boss, call me CEO, you a fake, just for show, trying to rap, but you too slow, I'm the king, you a clown, bro.",
    "Your game's so lame, it's a crying shame, I'm in the hall of fame, you're just a name, trying to play the same, but you got no flame.",
    "Your rhymes are stale, like day-old bread, I'm gourmet, you're just misled, try to flex, but end up dead, I'm living large, you're underfed.",
    "You're the joke, I'm the punchline, every battle, every time, step to me, it's a crime, I'm prime time, you're past your prime.",
    "I'm the main course, you're a side dish, got the vision, you just wish, I'm the truth, you're a fish, lost at sea, on my blacklist.",
    "Your style's so weak, it's hardly there, I'm the fresh air, you're just despair, try to compete, if you dare, I'll roast you hard, you better beware.",
    "My rhymes are fire, your lines are dire, I'm the supplier, you're just a crier, in this game, I'm the high-flyer, you crash and burn, perpetual liar.",
    "Step back, you ain't ready for this, my words hit like a heavyweight fist, you're dismissed, from the A-list, I'm the GOAT, you barely exist.",
    "You talking big, but can't walk the walk, I'm the truth, you're just talk, in this game, I'm a hawk, you're a mouse, better check the clock.",
    "You claim you're tough, but you're just fluff, I spit gold, you spit stuff, enough's enough, you ain't rough, I'm the diamond, you're the dust.",
    "You look like an extra from the Ant Movie, trying to flex but you just look goofy, I'm the star, you're a spoof, see, this roast is truth, G.",
    "Your time's up, like a broken clock, my rhymes tick-tock, you just stop, you a flop, I'm hip-hop, at the top, non-stop.",
    "You so slow, you make snails look fast, your best days are in the past, step to me, you won't last, I'm the future, you're the last.",
    "Your bars are weak, like WiFi in the sticks, my lines connect, your flow just ticks, trying to rap, but you need tricks, I'm the real deal, you need a fix.",
    "You got the style of a decade ago, I'm fresh and new, you don't even know, step back, enjoy the show, I'm the pro, you're just low.",
    "You look like you got dressed in the dark, my style's bright, you missed the mark, I'm the bite, you're just a bark, in this game, I'm the shark.",
    "Your flow's expired, like milk left out, my rhymes are fresh, without a doubt, you just pout, while I shout, my skills make the crowd jump and shout.",
    "You rap like a robot, stuck on repeat, I'm the real deal, bringing the heat, your defeat, can't compete, take a seat, admit defeat.",
    "You stuck in the past, like a VHS, I'm the future, in high def, your style's a mess, I confess, I'm the best, no contest."
]

copied_lines = {}

for index, line in enumerate(rap_lines):
    copied_lines[index] = []
    button = tk.Button(scrollable_frame, text=line, command=lambda idx=index: copy_to_clipboard(idx), wraplength=700, justify='left')
    button.pack(padx=5, pady=5, fill='x')

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

root.mainloop()
