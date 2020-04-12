from unittest import mock

from fluffy import cli
from fluffy import utils


@mock.patch.object(utils, 'get_pi', return_value=3.14)
@mock.patch.object(utils, 'add')
def test_main(add_, pi_):
    cli.main()

    add_.called_once()
    pi_.called_once()
