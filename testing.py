import unittest
import color_test


class UnitTestClass(unittest.TestCase):
    def test_Count_Pixel(self):
        f_performed = color_test.Count_Pixel('#ffffff', 'test_programme_file.jpg')
        self.assertEqual(f_performed, (15289, 6, 6, 'Чёрных пикселей больше'))
        f_performed = color_test.Count_Pixel('#000000', 'test_programme_file.jpg')
        self.assertEqual(f_performed, (15289, 6, 15289, 'Чёрных пикселей больше'))

    def test_color_input_validation(self):
        f_performed = color_test.color_input_validation('#ffffff')
        self.assertEqual(f_performed, True)
        f_performed = color_test.color_input_validation('#000000')
        self.assertEqual(f_performed, True)
        f_performed = color_test.color_input_validation('000000')
        self.assertEqual(f_performed, False)
        f_performed = color_test.color_input_validation('#0000000')
        self.assertEqual(f_performed, False)
        f_performed = color_test.color_input_validation('#f')
        self.assertEqual(f_performed, False)
        f_performed = color_test.color_input_validation('#jjjjjj')
        self.assertEqual(f_performed, False)

    def test_hex_to_rgb(self):
        f_performed = color_test.hex_to_rgb('#ffffff')
        self.assertEqual(f_performed, (255, 255, 255))
        f_performed = color_test.hex_to_rgb('#000000')
        self.assertEqual(f_performed, (0, 0, 0))
        f_performed = color_test.hex_to_rgb('#ff00ff')
        self.assertEqual(f_performed, (255, 0, 255))
        f_performed = color_test.hex_to_rgb('#f0f0f0')
        self.assertEqual(f_performed, (240, 240, 240))

    def test_rgb2hex(self):
        f_performed = color_test.rgb2hex(255, 255, 255)
        self.assertEqual(f_performed, '#ffffff')
        f_performed = color_test.rgb2hex(0, 0, 0)
        self.assertEqual(f_performed, '#000000')
        f_performed = color_test.rgb2hex(255, 0, 255)
        self.assertEqual(f_performed, '#ff00ff')
        f_performed = color_test.rgb2hex(240, 240, 240)
        self.assertEqual(f_performed, '#f0f0f0')


if __name__ == "__main__":
    unittest.main()
