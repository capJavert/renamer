import click
from click.testing import CliRunner


def test_cat():
    @click.command()
    @click.argument('file', type=click.File())
    def cat(file):
        click.echo(file.read())

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open('hello.txt', 'w') as f:
            f.write('Hello World!')

        result = runner.invoke(cat, ['hello.txt'])
        assert result.exit_code == 0
        assert result.output == 'Hello World!\n'


def test_prompts():
    @click.command()
    @click.option('--foo', prompt=True)
    def test(foo):
        click.echo('foo=%s' % foo)

    runner = CliRunner()
    result = runner.invoke(test, input='wau wau\n')
    assert not result.exception
    assert result.output == 'Foo: wau wau\nfoo=wau wau\n'
