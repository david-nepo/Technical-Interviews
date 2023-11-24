"""Main script for technical interview."""


def make_uppercase(input: str) -> str:
    """Makes string upper case."""

    return input.upper()


def split_into_names(input: str) -> list[str]:
    """Splits input strings into list of strings."""

    return input.split(';')


def reformat_name(name: str) -> str:
    """Reorders and reformats names."""

    first_name, last_name = name.split(':')
    formatted_name = f"({last_name}, {first_name})"

    return formatted_name


def sort_names_alphabetically(names: list[str]) -> list[str]:
    """Sorts names in alphabetical order."""

    return sorted(names)


def join_elements_in_list(names: list[str]) -> str:
    """Joins names in list together with no spaces."""

    return ''.join(names)


def main():
    """Main script logic."""

    input = "Fred:Corwill;Wilfred:Corwill;Barney:Tornbull;Betty:Tornbull;Bjon:Tornbull;Raphael:Corwill;Alfred:Corwill"

    guest_list = make_uppercase(input)

    guest_list = split_into_names(guest_list)

    formatted_guest_list = [reformat_name(name) for name in guest_list]

    sorted_guest_list = sort_names_alphabetically(formatted_guest_list)

    output_guest_list = join_elements_in_list(sorted_guest_list)

    print(input)
    print()
    print(output_guest_list)


if __name__ == "__main__":
    main()
