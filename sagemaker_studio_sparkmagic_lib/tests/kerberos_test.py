from sagemaker_studio_sparkmagic_lib import kerberos


def test_generated_krb_conf():
    krb_props = {
        "realms": {
            "EC2.INTERNAL": {
                "kdc": "ip-172-31-0-207.us-east-2.compute.internal:88",
                "admin_server": "ip-172-31-0-207.us-east-2.compute.internal:749",
                "default_domain": "us-east-2.compute.internal",
            },
            "KOLLOJUN.NET": {
                "kdc": "kollojun.net",
                "admin_server": "kollojun.net",
                "default_domain": "kollojun.net",
            },
        },
        "libdefaults": {"default_realm": "EC2.INTERNAL", "ticket_lifetime": "24h"},
        "domain_realm": {
            "us-east-2.compute.internal": "EC2.INTERNAL",
            ".us-east-2.compute.internal": "EC2.INTERNAL",
            ".kollojun.net": "KOLLOJUN.NET",
            "kollojun.net": "KOLLOJUN.NET",
        },
    }
    result = kerberos.generate_kerb_conf_str(krb_props)
    print(result)

    # copied from test emr cluster
    expected_conf = """# Generated by SageMaker helper library
[libdefaults]
    default_realm = EC2.INTERNAL
    dns_lookup_realm = false
    dns_lookup_kdc = false
    rdns = false
    ticket_lifetime = 24h
    forwardable = true
    udp_preference_limit = 1000000
    default_tkt_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1
    default_tgs_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1
    permitted_enctypes = aes256-cts-hmac-sha1-96 aes128-cts-hmac-sha1-96 des3-cbc-sha1

[realms]
    EC2.INTERNAL = {
        kdc = ip-172-31-0-207.us-east-2.compute.internal:88
        admin_server = ip-172-31-0-207.us-east-2.compute.internal:749
        default_domain = us-east-2.compute.internal
    }
    KOLLOJUN.NET = {
        kdc = kollojun.net
        admin_server = kollojun.net
        default_domain = kollojun.net
    }

[domain_realm]
    us-east-2.compute.internal = EC2.INTERNAL
    .us-east-2.compute.internal = EC2.INTERNAL
    .kollojun.net = KOLLOJUN.NET
    kollojun.net = KOLLOJUN.NET

"""

    assert result == expected_conf
