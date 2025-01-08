from ehrql import codelist_from_csv

adhd_codelist = codelist_from_csv(
    "codelists/nhsd-primary-care-domain-refsets-adhd_cod.csv",
    column="code",
)

methylphenidate_codelist = codelist_from_csv(
    "codelists/opensafely-methylphenidate-dmd.csv",
    column="code",
)