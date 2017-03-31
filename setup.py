from distutils.core import setup
setup(
          name = 'cl3ver',
          packages = ['cl3ver'],
          license = 'MIT',
          install_requires = ['requests'],
          version = '0.2',
          description = 'A python 3 wrapper for the cleverbot.com API',
          author = 'Japhy Bartlett',
          author_email = 'cl3ver@pearachute.com',
          url = 'https://github.com/japherwocky/cl3ver',
          download_url = 'https://github.com/japherwocky/cl3ver/tarball/0.2.tar.gz',
          keywords = ['cleverbot', 'wrapper', 'clever', 'chatbot', 'cl3ver'],
          classifiers =[
              'Programming Language :: Python :: 3 :: Only',
              'License :: OSI Approved :: MIT License',
              'Intended Audience :: Developers',
              'Natural Language :: English',
          ],
)
