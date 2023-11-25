import customtkinter
from customtkinter import (
    CTkButton,
    CTkCheckBox,
    CTkOptionMenu,
    CTkSlider,
    CTkSwitch,
    StringVar,
)
from collections import namedtuple
from typing import Any, Union


customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")


class EpicGamesGUI:
    app = customtkinter.CTk()
    # app.geometry("640x480")

    # DEFINITIONS
    # customtkinter.set_window_scaling(0.5)
    # customtkinter.set_widget_scaling(0.5)

    # define button
    DefinedButton = namedtuple(
        "DefinedButton", ["name", "command", "relx", "rely", "anchor"]
    )
    DefinedButton.__new__.__defaults__ = ("",) * len(DefinedButton._fields)

    # define option menu
    DefinedOptionMenu = namedtuple(
        "DefinedOptionMenu",
        ["relx", "rely", "anchor"],
    )
    DefinedOptionMenu.__new__.__defaults__ = ("",) * len(DefinedOptionMenu._fields)

    # define checkbox
    DefinedCheckBox = namedtuple(
        "DefinedCheckBox",
        ["text", "command", "onvalue", "offvalue", "relx", "rely", "anchor"],
    )
    DefinedCheckBox.__new__.__defaults__ = ("",) * len(DefinedCheckBox._fields)

    # define a slider
    DefinedSlider = namedtuple(
        "DefinedSlider", ["from_", "to_", "command", "relx", "rely", "anchor"]
    )

    # define pack
    DefinedPack = namedtuple("DefinedPack", ["padx", "pady"])
    DefinedPack.__new__.__defaults__ = (0,) * len(DefinedPack._fields)

    # define grid
    DefinedGrid = namedtuple("DefinedGrid", ["row", "column", "padx", "pady"])
    DefinedGrid.__new__.__defaults__ = (0,) * len(DefinedGrid._fields)

    def __init__(self) -> None:
        self.create_app()
        self.app.mainloop()

    def create_app(self):
        # Select Retailer
        self.grid(
            self.option_menu(
                ["EpicGames", "Steam(Experimental)"],
                self.DefinedOptionMenu(
                    relx=3,
                    rely=3,
                    anchor="w",
                ),
            ),
            self.DefinedGrid(0, 0, 10, 10),
        )
        # save, open direct
        self.grid(
            self.option_menu(
                ["Save and Open", "Just Save", "Open Directly"],
                self.DefinedOptionMenu(
                    relx=3,
                    rely=3,
                    anchor="w",
                ),
            ),
            self.DefinedGrid(1, 0, 10, 10),
        )

        # send mail or not
        checkboxWidget = self.grid(
            self.checkbox(
                self.DefinedCheckBox(
                    text="Send Mail?",
                    command=self._checkbox_callback,
                    onvalue="on",
                    offvalue="off",
                    relx=3,
                    rely=3,
                    anchor="w",
                )
            ),
            self.DefinedGrid(2, 0, 10, 10),
        )

        # create button pack
        self.grid(
            self.button(
                self.DefinedButton("CustomButton", self._custom_button, 0.5, 0.5, "s")
            ),
            self.DefinedGrid(4, 0, 10, 10),
        )

    def button(self, button: DefinedButton) -> CTkButton:
        confirm_button = customtkinter.CTkButton(
            master=self.app, text=button.name, command=button.command
        )
        confirm_button.place(
            relx=button.relx,
            rely=button.rely,
            anchor=button.anchor,
        )
        return confirm_button

    def option_menu(self, options: list, option: DefinedOptionMenu) -> CTkOptionMenu:
        optionMenu = CTkOptionMenu(
            master=self.app,
            values=options,
            # NOTE: define command directly because
            # we need to define custom option menu for prevent empty menu items
            command=self._optionmenu_callback,
        )
        optionMenu.place(
            relx=option.relx,
            rely=option.rely,
            anchor=option.anchor,
        )
        return optionMenu

    def checkbox(self, vars: DefinedCheckBox) -> CTkCheckBox:
        check_var = StringVar(value="off")
        checkboxButton = CTkCheckBox(
            master=self.app,
            text=vars.text,
            variable=check_var,
            command=lambda: vars.command(check_var),
            onvalue=vars.onvalue,
            offvalue=vars.offvalue,
        )

        checkboxButton.place(
            relx=vars.relx,
            rely=vars.rely,
            anchor=vars.anchor,
        )

        return checkboxButton

    def pack(self, obj: Union[CTkButton, CTkOptionMenu, Any], pack: DefinedPack):
        return obj.pack(padx=pack.padx, pady=pack.pady)

    def grid(self, obj: Union[CTkButton, CTkOptionMenu, Any], _grid: DefinedGrid):
        return obj.grid(
            row=_grid.row, column=_grid.column, padx=_grid.padx, pady=_grid.pady
        )

    @classmethod
    def _custom_button(cls):
        print("yoooo")

    @classmethod
    def _optionmenu_callback(cls, choice):
        print("choice is ", choice)

    @classmethod
    def _checkbox_callback(cls, val):
        print("toogled", val.get())

    # @classmethod
    # def _slider_callback(cls, val):
    #     print("slider value", val)


if __name__ == "__main__":
    EpicGamesGUI()
