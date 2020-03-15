import click
from logic import selenium_sequence, selenium_sequence_track_list, process_entries
from charts import pie_related, pie_sale, pie_sold_out


@click.group()
def manager():
    pass


@manager.command()
@click.option("--chart", "-ch", type=click.Choice(["related", "sale", "soldout"]))
@click.option(
    "--count", "-c",
)
@click.option("--tlist", "-t")
@click.argument("query", nargs=-1)
def blacktears(chart, count, query, tlist):
    if chart and count and query:
        pseudo_switch = {
            "related": pie_related,
            "sale": pie_sale,
            "soldout": pie_sold_out,
        }
        pseudo_switch.get(chart)(query, int(count))
    elif count and query:
        selenium_sequence(query, int(count))
    elif tlist and query:
        selenium_sequence_track_list(query, tlist)
