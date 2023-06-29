import decoder


if __name__ == "__main__":
    decoder_class = decoder.DecodeSensor()
    decoded_data = decoder_class.decoder_from_sensor('27C7011D')
    print(decoded_data)
