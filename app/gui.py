import tkinter as tk
from scoring_engine import calculate_score
from recommendations import generate_recommendations


def start_gui():

    window = tk.Tk()

    window.title("RansomShield")
    window.geometry("600x500")


    title = tk.Label(
        window,
        text="RansomShield\nRansomware Protection Assessment",
        font=("Arial",16)
    )

    title.pack(pady=20)


    antivirus = tk.BooleanVar()
    backup = tk.BooleanVar()
    mfa = tk.BooleanVar()
    monitoring = tk.BooleanVar()


    tk.Checkbutton(
        window,
        text="Antivirus Enabled",
        variable=antivirus
    ).pack()


    tk.Checkbutton(
        window,
        text="Backup Enabled",
        variable=backup
    ).pack()


    tk.Checkbutton(
        window,
        text="Multi-Factor Authentication",
        variable=mfa
    ).pack()


    tk.Checkbutton(
        window,
        text="File Monitoring",
        variable=monitoring
    ).pack()



    result = tk.Label(window,text="")

    result.pack(pady=20)



    def assess():

        score = calculate_score(
            antivirus.get(),
            backup.get(),
            mfa.get(),
            monitoring.get()
        )


        recommendations = generate_recommendations(
            antivirus.get(),
            backup.get(),
            mfa.get(),
            monitoring.get()
        )


        result.config(
            text=f"""
Protection Score:
{score}/100


Recommendations:

{recommendations}
"""
        )


    tk.Button(
        window,
        text="Run Assessment",
        command=assess
    ).pack()



    window.mainloop()
