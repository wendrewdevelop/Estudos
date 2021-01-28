CREATE TABLE etl_teste (
	UNIQUE_ID INTEGER NOT NULL,
	TRANSACTION_DATE VARCHAR(20) NOT NULL,
	CLIENT_ID INTEGER NOT NULL,
	TRANSACTION_ID INTEGER NOT NULL,
	BANK_TRANSACTION_ID INTEGER,
	ORGANIZATION_ID INTEGER,
	PARTNER_ID INTEGER,
	STORE_ID INTEGER,
	CLIENT_CODE VARCHAR(255) NOT NULL,
	ACQUIRER_ID INTEGER NOT NULL,
	ACQUIRER_NAME VARCHAR(255) NOT NULL,
	MERCHANT_ID INTEGER NOT NULL,
	SALE_DATE VARCHAR(20),
	FORECAST_DATE VARCHAR(20),
	DOC_NUMBER INTEGER NOT NULL,
	POS_NUMBER INTEGER,
	DESCRIPTION VARCHAR(255),
	SUMMARY INTEGER NOT NULL,
	UK_SUMMARY INTEGER NOT NULL,
	UK_TRANSACTION INTEGER NOT NULL,
	BANK_CODE INTEGER NOT NULL,
	BANK_BRANCH INTEGER NOT NULL,
	BANK_ACCOUNT INTEGER NOT NULL,
	EVENT_TYPE VARCHAR(255) NOT NULL,
	TRANSACTION_CODE VARCHAR(255) NOT NULL,
	EVENT_DESCRIPTION VARCHAR(255) NOT NULL,
	CLASSIFICATION VARCHAR(255) NOT NULL,
	SIGN VARCHAR(10) NOT NULL,
	LINK_PAYMENT_DETAIL VARCHAR(255) NOT NULL,
	TRANSACTION_TYPE VARCHAR(255) NOT NULL,
	SETTLEMENT_TYPE VARCHAR(255) NOT NULL,
	ADVANCE_PAYMENT_TYPE VARCHAR(255),
	FILE_NAME VARCHAR(255) NOT NULL,
	FILE_SEQUENCE INTEGER NOT NULL,
	FILE_NUMBER INTEGER NOT NULL,
	LINE_NUMBER INTEGER NOT NULL,
	RECONCILE_ID INTEGER NOT NULL,
	GL_DATE VARCHAR(20) NOT NULL,
	EXPECTED_CLEARING_DATE VARCHAR(20) NOT NULL,
	PAYMENT_DATE VARCHAR(20) NOT NULL,
	CLEARING_DATE VARCHAR(20) NOT NULL,
	RECEIPT_AMOUNT VARCHAR(255) NOT NULL,
	BANK_DOC_NUMBER VARCHAR(255),
	BANK_DESCRIPTION VARCHAR(255),
	DEPOSIT_DATE VARCHAR(255),
	DEPOSIT_AMOUNT VARCHAR(255),
	BANK_SIGN VARCHAR(255),
	CREATED_AT VARCHAR(255),
	STORE_NAME VARCHAR(255)
	
)

SELECT * FROM etl_teste;