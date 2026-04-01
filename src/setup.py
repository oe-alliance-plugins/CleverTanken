from setuptools import setup
import setup_translate

pkg = 'Extensions.CleverTanken'
setup(name='enigma2-plugin-extensions-clevertanken',
       version='3.0',
       description='Clever Tanken Plugin',
       package_dir={pkg: 'CleverTanken'},
       packages=[pkg],
       package_data={pkg: ['images/*.png', '*.png', '*.xml', 'locale/*/LC_MESSAGES/*.mo', 'pic/*.png']},
       cmdclass=setup_translate.cmdclass,  # for translation
      )
