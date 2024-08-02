import machine
import utime

# RGB LEDのPWM設定
red = machine.PWM(machine.Pin(13))
green = machine.PWM(machine.Pin(14))
blue = machine.PWM(machine.Pin(15))
red.freq(1000)
green.freq(1000)
blue.freq(1000)

# 値の範囲をマッピングする関数
def interval_mapping(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# 色の値をPWMのduty値に変換する関数
def color_to_duty(rgb_value):
    rgb_value = int(interval_mapping(rgb_value, 0, 255, 0, 65535))
    return rgb_value

# RGB LEDの色を設定する関数
def color_set(red_value, green_value, blue_value):
    red.duty_u16(color_to_duty(red_value))
    green.duty_u16(color_to_duty(green_value))
    blue.duty_u16(color_to_duty(blue_value))

# メインループ
while True:
    print("1. Red\n"
          "2. Green\n"
          "3. Blue\n"
          "4. Off\n"
          "5. Quit\n"
          )

    option = input("Select an option: ")

    if option == "1":
        # 赤色に設定
        color_set(255, 0, 0)

    elif option == "2":
        # 緑色に設定
        color_set(0, 255, 0)

    elif option == "3":
        # 青色に設定
        color_set(0, 0, 255)

    elif option == "4":
        # 消灯
        color_set(0, 0, 0)

    elif option == "5":
        print("Exiting the menu.")
        break

    else:
        print("Please try again.")
