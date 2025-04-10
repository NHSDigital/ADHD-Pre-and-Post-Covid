# NHS England ADHD OpenSAFELY Analysis Project 

> [!WARNING]  
> This repository is in active development and contents of this repository MUST NOT be considered an accurate or valid representation of the study or its purpose. This repository may reflect an incomplete or incorrect analysis with no further ongoing work. The content has ONLY been made public to support the OpenSAFELY [open science and transparency principles](https://www.opensafely.org/about/#contributing-to-best-practice-around-open-science) and to support the sharing of re-usable code for other subsequent users. No clinical, policy or safety conclusions must be drawn from the contents of this repository.

This repo is codebase for the approved [OpenSAFELY project #181: Examining changes in ADHD diagnosis and pathways in primary care pre and post COVID pandemic](https://www.opensafely.org/approved-projects/#project-181)

Detail description of the project can be found on our [protocol]( https://github.com/opensafely/ADHD-Pre-and-Post-Covid/tree/main/protocol%20)

Each query is logged in [OpenSAFELY Jobs](https://jobs.opensafely.org/examining-changes-in-adhd-diagnosis-and-pathways-in-primary-care-pre-and-post-covid-pandemic/adhd-pre-and-post-covid/) 



## Prerequisites

The repo can be run on [dummy data](https://docs.opensafely.org/ehrql/how-to/dummy-data/) using [GitHub Codespaces]( https://docs.opensafely.org/getting-started/how-to/use-github-codespaces-in-your-project/)

The [metadata of clinical code]( https://www.opencodelists.org/) used in this study can be found in our [Codelist file]( https://github.com/opensafely/ADHD-Pre-and-Post-Covid/blob/main/analysis/codelists.py).

## Compliance

The project is performed under the [OpenSAFELY COVID-19 Service]( https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice) thus may be subject to a [legal hold](https://transform.england.nhs.uk/documents/147/PRN00309_ii_Example_document_preservation_notice_210323_Open_access_Word_file_MASTER.odt) from the [Transformation Directorate]( https://transform.england.nhs.uk/information-governance/guidance/preparing-for-the-uk-covid-19-inquiry/)

The work is [backup]( https://github.com/NHSDigital/ADHD-Pre-and-Post-Covid) automatically [every 24 hours](https://github.com/NHSDigital/ADHD-Pre-and-Post-Covid/actions) to [NHS England previously NHS Digital’s GitHub organization]( https://github.com/NHSDigital).


## Licence

Unless stated otherwise, the codebase is released under the MIT License.

Any HTML or Markdown documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0 licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).


## Contact
This repository is partly maintained by the [NHS England Data Science Team][ds-email]. To contact us - [email][ds-email]. 

See our other work on the [NHS England Data Science website][ds-site].

## About the OpenSAFELY framework

The OpenSAFELY framework is a secure analytics platform for
electronic health records research in the NHS.

Instead of requesting access for slices of patient data and
transporting them elsewhere for analysis, the framework supports
developing analytics against dummy data, and then running against the
real data *within the same infrastructure that the data is stored*.
Read more at [OpenSAFELY.org](https://opensafely.org).

---
[ds-site]: https://nhsengland.github.io/datascience/
[ds-email]: mailto:datascience@nhs.net
