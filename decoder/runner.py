import os
import decoder


if __name__ == "__main__":
    decoder_class = decoder.decodeSensor()
    decoder_class.decoder_from_sensor('27C7011D')
    print("something")
