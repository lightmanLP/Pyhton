import dataclasses
import timeit
import random  # noqa: F401


__doc__ = """timeit of random for Maybe"""


@dataclasses.dataclass
class Test:
    setup: str
    code: str
    time: float = -.0
    number: int = 100000
    results: list = dataclasses.field(default_factory=list)

    def run(self):
        self.time = timeit.timeit(
            self.code,
            setup=self.setup,
            number=self.number
        )
        self.results = tuple(eval(self.code) for _ in range(10000))

    def show(self) -> None:
        print(
            f"time: {self.time}\n"
            f"code: {self.code}\n"
            f"{self.results.count(True): >4} True"
            " | "
            f"{self.results.count(False): >4} False",
            end="\n\n"
        )


tests = [
    Test(
        setup="import random",
        code="bool(random.randint(0, 1))",
    ),
    Test(
        setup="import random",
        code="bool(random.choice((True, False)))",
    ),
    Test(
        setup="import random",
        code="bool(random.getrandbits(1))",
    ),
]
for test in tests:
    test.run()

tests = sorted(tests, key=lambda o: o.time)

for i in tests:
    i.show()

print(f"fastest: {tests[0].code}")
