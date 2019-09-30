import click
import pkg_resources

from lib.convert_html_to_jpeg.convert_html_to_jpeg import convert_html_to_jpeg as chtj


@click.command()
@click.option('-n', help='Name of the output file')
@click.argument('html_file')
def html_to_jpeg(n, html_file):
    """Convert HTML page into a jpeg file"""
    my_chtj = chtj(html_file)
    my_chtj.convert(name=n)

