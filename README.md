# NHS England ADHD OpenSAFELY Analysis Project 

> [!WARNING]  
> This repository is in active development and contents of this repository MUST NOT be considered an accurate or valid representation of the study or its purpose. This repository may reflect an incomplete or incorrect analysis with no further ongoing work. The content has ONLY been made public to support the OpenSAFELY [open science and transparency principles](https://www.opensafely.org/about/#contributing-to-best-practice-around-open-science) and to support the sharing of re-usable code for other subsequent users. No clinical, policy or safety conclusions must be drawn from the contents of this repository.

> [!NOTE]  
> Initial results will appear on the [ADHD Management Information - November 2025](https://digital.nhs.uk/data-and-information/publications/statistical/mi-adhd/november-2025) on 4th Dec 2025.

This repo is the [open codebase](https://www.gov.uk/service-manual/service-standard/point-12-make-new-source-code-open) for the approved [OpenSAFELY project #181: Examining changes in ADHD diagnosis and pathways in primary care pre and post COVID pandemic](https://www.opensafely.org/approved-projects/#project-181). 

Work is carried out by the [NHS England Data Science Team][ds-site]

Detail description of the project can be found on our [protocol]( https://github.com/opensafely/ADHD-Pre-and-Post-Covid/tree/main/protocol)

Each query is logged in [OpenSAFELY Jobs](https://jobs.opensafely.org/examining-changes-in-adhd-diagnosis-and-pathways-in-primary-care-pre-and-post-covid-pandemic/) 

This repo aims to be at [Baseline level RAP](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/#baseline-rap-getting-the-fundamentals-right)

## Contact

Email: [datascience@nhs.net][ds-email] 

## Prerequisites

The repo can be run on [dummy data](https://docs.opensafely.org/ehrql/how-to/dummy-data/) using [GitHub Codespaces]( https://docs.opensafely.org/getting-started/how-to/use-github-codespaces-in-your-project/)

### Metadata

The [metadata of clinical codes]( https://www.opencodelists.org/) used in this study are followed:
* [Attention Deficit Hyperactivity Disorder codes](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/adhd_cod/20200812/)
* [Attention Deficit Hyperactivity Disorder in remission codes](https://www.opencodelists.org/codelist/nhsd-primary-care-domain-refsets/adhdrem_cod/20200812/)
* [Attention Deficit Hyperactivity Disorder Medication](https://www.opencodelists.org/codelist/user/Adam/adhd-dmd/59d39fe1/#full-list)

## Supplementary Materials
The repo contains the following supporting documentation found in [docs]( docs)
* [ADHD Prevalence in EMIS and Cegedim]( docs/emis_calculation)
* [Usage of ADHD Remission Codes from 2023 to 2024]( docs/remission_calculation)
* [Code to Plot Graphs]( docs/graph_production)
* [SNOMED Code for ADHD Suspected]( docs/adhd_suspected)
* [Output CSV Postprocessing]( docs/csv_postprocessing)

## Compliance

The project is performed under the [OpenSAFELY COVID-19 Service]( https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/directions-and-data-provision-notices/data-provision-notices-dpns/opensafely-covid-19-service-data-provision-notice) thus may be subject to a [legal hold](https://transform.england.nhs.uk/documents/147/PRN00309_ii_Example_document_preservation_notice_210323_Open_access_Word_file_MASTER.odt) from the [Transformation Directorate]( https://transform.england.nhs.uk/information-governance/guidance/preparing-for-the-uk-covid-19-inquiry/)

The work is [backup]( https://github.com/NHSDigital/ADHD-Pre-and-Post-Covid) automatically [every 24 hours](https://github.com/NHSDigital/ADHD-Pre-and-Post-Covid/actions) to [NHS England previously NHS Digital’s GitHub organization]( https://github.com/NHSDigital).


## Licence

Unless stated otherwise, the codebase is released under the MIT License.

Any HTML or Markdown documentation is [© Crown copyright](https://www.nationalarchives.gov.uk/information-management/re-using-public-sector-information/uk-government-licensing-framework/crown-copyright/) and available under the terms of the [Open Government 3.0 licence](https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/).


## NHS England Data Science Team
This repository is partly maintained by the [NHS England Data Science Team][ds-email].

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
