import click
import pipexample

@click.command()
@click.argument("num")
def main(num):
  foo = pipexample.Foo(num)
  print foo.x

  print pipexample.readme()

if __name__ == "__main__":
  main()


