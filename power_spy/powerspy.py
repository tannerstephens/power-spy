from time import sleep

from gpiozero import LED, Button


def is_pc_on():
    power_status = Button(12, pull_up=False)

    ret_value = power_status.is_active

    power_status.close()

    return ret_value


def press_power_button():
    power_button = LED(25)

    power_button.on()
    sleep(0.1)
    power_button.off()

    power_button.close()

def hard_reboot():
    power_button = LED(25)

    power_button.on()
    sleep(6)
    power_button.off()

    power_button.close()
