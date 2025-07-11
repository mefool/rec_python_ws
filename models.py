from pydantic import BaseModel
from typing import Optional

class RecComplete(BaseModel):
    # Section 0. Subject
    # tk_XX: Optional[str] = None   # Initial Mapping 
    # Section 1. Subject of this Agreement and Interpretation
    tk_52:  Optional[str] = None	# agreement_effective_date
    # Section 2. Trade Identification
    tk_455: Optional[str] = None	# trade_identifier
    # Section 3. Seller
    tk_437: Optional[str] = None	# seller_registry_operator
    tk_438: Optional[str] = None	# seller_registry_eecs_reg_db
    tk_439: Optional[str] = None	# seller_registry_account
    tk_440: Optional[str] = None	# seller_bank_vat
    tk_441: Optional[str] = None	# seller_bank_iban
    tk_442: Optional[str] = None	# seller_bank_bic_swift_code
    tk_443: Optional[str] = None	# seller_bank_account
    tk_444: Optional[str] = None	# seller_bank_name
    tk_445: Optional[str] = None	# seller_contact_email
    tk_446: Optional[str] = None	# seller_contact_fax
    tk_447: Optional[str] = None	# seller_contact_phone
    tk_448: Optional[str] = None	# seller_contact_name
    tk_449: Optional[str] = None	# seller_address_country
    tk_450: Optional[str] = None	# seller_address_town
    tk_451: Optional[str] = None	# seller_address_postalcode
    tk_452: Optional[str] = None	# seller_address_street
    tk_453: Optional[str] = None	# seller_registration_nr
    tk_454: Optional[str] = None	# seller_company
    # Section 3. Trade Identification
    tk_889: Optional[str] = None	# buyer_registry_operator
    tk_890: Optional[str] = None	# buyer_registry_eecs_reg_db
    tk_891: Optional[str] = None	# buyer_registry_account
    tk_892: Optional[str] = None	# buyer_bank_vat
    tk_893: Optional[str] = None	# buyer_bank_iban
    tk_894: Optional[str] = None	# buyer_bank_bic_swift_code
    tk_895: Optional[str] = None	# buyer_bank_account
    tk_896: Optional[str] = None	# buyer_bank_name
    tk_897: Optional[str] = None	# buyer_contact_email
    tk_898: Optional[str] = None	# buyer_contact_fax
    tk_899: Optional[str] = None	# buyer_contact_phone
    tk_900: Optional[str] = None	# buyer_contact_name
    tk_901: Optional[str] = None	# buyer_address_country
    tk_902: Optional[str] = None	# buyer_address_town
    tk_903: Optional[str] = None	# buyer_address_postalcode
    tk_904: Optional[str] = None	# buyer_address_street
    tk_905: Optional[str] = None	# buyer_registration_nr
    tk_906: Optional[str] = None	# buyer_company
    tk_272: Optional[str] = None	# total_contract_price
    tk_273: Optional[str] = None	# total_quantity
    # Section 5. Transaction Details
    currency: Optional[str] = None  # currency
    group1_int: Optional[str] = None	# cert_eecs_go_or_disclosure
    tk_336: Optional[str] = None	# table_02F
    tk_337: Optional[str] = None	# table_02E
    tk_338: Optional[str] = None	# table_02D
    tk_339: Optional[str] = None	# table_02C
    tk_340: Optional[str] = None	# table_02B
    tk_341: Optional[str] = None	# table_02A
    tk_342: Optional[str] = None	# table_01F_contract_price
    tk_343: Optional[str] = None	# table_01E_certif_price
    tk_344: Optional[str] = None	# table_01D_quantity
    tk_345: Optional[str] = None	# table_01C_deliverydate
    tk_346: Optional[str] = None	# table_01B_tech
    tk_347: Optional[str] = None	# table_01A_prod_period
    tk_475: Optional[str] = None	# earmark
    tk_476: Optional[str] = None	# minimum_validity_certif
    tk_720: Optional[str] = None	# independent_criteria_scheme
    tk_817: Optional[str] = None	# table_04F
    tk_818: Optional[str] = None	# table_04E
    tk_819: Optional[str] = None	# table_04D
    tk_820: Optional[str] = None	# table_04C
    tk_821: Optional[str] = None	# table_04B
    tk_822: Optional[str] = None	# table_04A
    tk_823: Optional[str] = None	# table_03F
    tk_824: Optional[str] = None	# table_03E
    tk_825: Optional[str] = None	# table_03D
    tk_826: Optional[str] = None	# table_03C
    tk_827: Optional[str] = None	# table_03B
    tk_828: Optional[str] = None	# table_03A
    tk_829: Optional[str] = None	# table_06F
    tk_830: Optional[str] = None	# table_06E
    tk_831: Optional[str] = None	# table_06D
    tk_832: Optional[str] = None	# table_06C
    tk_833: Optional[str] = None	# table_06B
    tk_834: Optional[str] = None	# table_06A
    tk_835: Optional[str] = None	# table_05F
    tk_836: Optional[str] = None	# table_05E
    tk_837: Optional[str] = None	# table_05D
    tk_838: Optional[str] = None	# table_05C
    tk_839: Optional[str] = None	# table_05B
    tk_840: Optional[str] = None	# table_05A
    tk_841: Optional[str] = None	# table_08F
    tk_842: Optional[str] = None	# table_08E
    tk_843: Optional[str] = None	# table_08D
    tk_844: Optional[str] = None	# table_08C
    tk_845: Optional[str] = None	# table_08B
    tk_846: Optional[str] = None	# table_08A
    tk_847: Optional[str] = None	# table_07F
    tk_848: Optional[str] = None	# table_07E
    tk_849: Optional[str] = None	# table_07D
    tk_850: Optional[str] = None	# table_07C
    tk_851: Optional[str] = None	# table_07B
    tk_852: Optional[str] = None	# table_07A
    tk_853: Optional[str] = None	# table_14F
    tk_854: Optional[str] = None	# table_14E
    tk_855: Optional[str] = None	# table_14D
    tk_856: Optional[str] = None	# table_14C
    tk_857: Optional[str] = None	# table_14B
    tk_858: Optional[str] = None	# table_14A
    tk_859: Optional[str] = None	# table_13F
    tk_860: Optional[str] = None	# table_13E
    tk_861: Optional[str] = None	# table_13D
    tk_862: Optional[str] = None	# table_13C
    tk_863: Optional[str] = None	# table_13B
    tk_864: Optional[str] = None	# table_13A
    tk_865: Optional[str] = None	# table_12F
    tk_866: Optional[str] = None	# table_12E
    tk_867: Optional[str] = None	# table_12D
    tk_868: Optional[str] = None	# table_12C
    tk_869: Optional[str] = None	# table_12B
    tk_870: Optional[str] = None	# table_12A
    tk_871: Optional[str] = None	# table_11F
    tk_872: Optional[str] = None	# table_11E
    tk_873: Optional[str] = None	# table_11D
    tk_874: Optional[str] = None	# table_11C
    tk_875: Optional[str] = None	# table_11B
    tk_876: Optional[str] = None	# table_11A
    tk_877: Optional[str] = None	# table_10F
    tk_878: Optional[str] = None	# table_10E
    tk_879: Optional[str] = None	# table_10D
    tk_880: Optional[str] = None	# table_10C
    tk_881: Optional[str] = None	# table_10B
    tk_882: Optional[str] = None	# table_10A
    tk_883: Optional[str] = None	# table_09F
    tk_884: Optional[str] = None	# table_09E
    tk_885: Optional[str] = None	# table_09D
    tk_886: Optional[str] = None	# table_09C
    tk_887: Optional[str] = None	# table_09B
    tk_888: Optional[str] = None	# table_09A
    tk_9010: Optional[str] = None	# transaction_qualities_type_of_support
    tk_9011: Optional[str] = None	# transaction_qualities_commisioning_date
    tk_908: Optional[str] = None	# transaction_qualities_max_greenhouse_emissions
    tk_909: Optional[str] = None	# transaction_special_conditions
    tk_910: Optional[str] = None	# domain_country_of_prod
    tk_911: Optional[str] = None	# domain_issuing_body_prod
    tk_912: Optional[str] = None	# domain_country_of_deliv
    tk_913: Optional[str] = None	# domain_issuing_body_deliv
    tk_914: Optional[str] = None	# production_device_name
    tk_915: Optional[str] = None	# production_device_number
    tk_916: Optional[str] = None	# production_device_adicional_info
    EUR: Optional[str] = None	    # currency
    # Section 6. Transfer Mechanism
    group2_int: Optional[str] = None	# transfer_eletronic_or_cancellation_statment
    # Section 24. Governing Law and Dispute Resolution
    tk_370: Optional[str] = None	# governing_law_accordance
    tk_723: Optional[str] = None	# governing_dispute_rules_of
    tk_724: Optional[str] = None	# governing_dispute_seat_arbitrator
    # Section 25. Special Conditions
    tk_367: Optional[str] = None	# special_conditions
    # Section 26. Authorised representatives
    tk_8010: Optional[str] = None	# buyer_2_date
    tk_8011: Optional[str] = None	# buyer_2_title
    tk_8012: Optional[str] = None	# seller_2_title
    tk_8013: Optional[str] = None	# buyer_1_date
    tk_8014: Optional[str] = None	# buyer_1_title
    tk_8015: Optional[str] = None	# seller_1_title
    tk_811: Optional[str] = None	# seller_2_date
    tk_812: Optional[str] = None	# buyer_2_name
    tk_813: Optional[str] = None	# seller_2_name
    tk_814: Optional[str] = None	# seller_1_date
    tk_815: Optional[str] = None	# buyer_1_name
    tk_816: Optional[str] = None	# seller_1_name