from distutils.core import setup
setup(
  name = 'nodebox_linguistics_extended',
  packages = ['nodebox_linguistics_extended'],
  package_data={'nodebox_linguistics_extended':      ['ogden/*','parser/*','parser/nltk_lite/*','parser/nltk_lite/chat/*','parser/nltk_lite/cluster/*','parser/nltk_lite/contrib/*','parser/nltk_lite/contrib/toolbox/*','parser/nltk_lite/corpora/*','parser/nltk_lite/draw/*','parser/nltk_lite/etree/*','parser/nltk_lite/misc/*','parser/nltk_lite/model/*','parser/nltk_lite/parse/*','parser/nltk_lite/semantics/*','parser/nltk_lite/stem/*','parser/nltk_lite/tag/*','parser/nltk_lite/test/*','parser/nltk_lite/tokenize/*','parser/nltk_lite/wordnet/*','spelling/*','verb/*','wordnet/*','wordnet/docs/*','wordnet/docsrc/*','wordnet/wordnet2/*','wordnet/wordnet2/dict/*','wordnet/wordnet2/doc/*','wordnet/wordnet2/doc/html/*','wordnet/wordnet2/doc/man/*','wordnet/wordnet2/doc/pdf/*','wordnet/wordnet2/doc/ps/*','wordnet/wordnet2/include/*','wordnet/wordnet2/lib/*','wordnet/wordnet2/lib/wnres/*','wordnet/wordnet2/src/*']},
  version = '0.0.1',
  description = 'Extension of the Nodebox Linguistics library',
  author = 'Sarah Harmon',
  author_email = 'sharmon@bowdoin.edu',
  license='GNU',
  url = 'https://github.com/RensaProject/nodebox_linguistics_extended',
  classifiers = [
    'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
  ],
  install_requires = [
    'sgmllib3k'
  ]
)
