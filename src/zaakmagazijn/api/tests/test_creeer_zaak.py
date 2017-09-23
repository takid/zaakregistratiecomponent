from unittest import skip

from lxml import etree

from zaakmagazijn.api.stuf.choices import BerichtcodeChoices
from zaakmagazijn.rgbz.models import (
    BuurtObject, KadastraalPerceelObject,
    OverigeAdresseerbaarObjectAanduidingObject, Rol, Zaak
)
from zaakmagazijn.rgbz.tests.factory_models import (
    MedewerkerFactory, OrganisatorischeEenheidFactory,
    OverigeAdresseerbaarObjectAanduidingObjectFactory, ZaakTypeFactory
)
from zaakmagazijn.rsgb.models import PostAdres

from .base import BaseTestPlatformTests


class MaykincreeerZaak_ZakLk01ZakObjectTests(BaseTestPlatformTests):
    test_files_subfolder = 'maykin_creeerZaak'
    porttype = 'OntvangAsynchroon'

    def setUp(self):
        super().setUp()

        # medewerker wordt geidentificeerd in de .xml bestanden, met
        # '${gemeentecode}56789' wat is vervangen door '0123456789'
        self.medewerker = MedewerkerFactory.create(
            organisatorische_eenheid__organisatieeenheididentificatie='01234',
            medewerkeridentificatie='56789')
        self.assertEqual(self.medewerker.identificatie, '0123456789')

        self.zaak_type = ZaakTypeFactory.create(
            zaaktypeomschrijving='Aanvraag burgerservicenummer behandelen',
            zaaktypeidentificatie='12345678')

        self.context = {
            'gemeentecode': '',
            'referentienummer': self.genereerID(10),

            'datumVandaag': self.genereerdatum(),
            'datumEergisteren': self.genereerdatum(-2),
            'tijdstipRegistratie': self.genereerdatumtijd(),

            'zds_zaaktype_omschrijving': 'Aanvraag burgerservicenummer behandelen',
            'zds_zaaktype_code': '12345678',
        }

    def test_create_buurt(self):
        self.context.update(**{
            'buurtcode': '12',
            'buurtnaam': 'Buurtnaam',
            'geometrie': '<gml>a</gml>',
            'gem_gemeente_code': '1234',
            'wijk_wijk_code': '12',
            'ingangsdatum_object': '20170902',
            'einddatum_object': '20170903',
            'genereerbesluitident_identificatie_2': '123',
            'genereerzaakident_identificatie_2': self.genereerID(10),
        })
        vraag = 'creeerZaak_ZakLk01_buurt.xml'
        response = self._do_request(self.porttype, vraag, self.context)

        # Only 1 BuurtObject should've been created.
        self.assertEquals(BuurtObject.objects.count(), 1)

        zaak = Zaak.objects.get()
        self.assertEquals(zaak.zaakobject_set.count(), 1)
        zaakobj = zaak.zaakobject_set.get()
        self.assertEquals(zaakobj.relatieomschrijving, 'omschrijving')
        obj = zaakobj.object
        buurt = obj.is_type()
        self.assertIs(type(buurt), BuurtObject)
        self.assertEquals(buurt.buurtcode, self.context['buurtcode'])
        self.assertEquals(buurt.buurtnaam, self.context['buurtnaam'])
        self.assertEquals(buurt.geometrie, self.context['geometrie'])
        self.assertEquals(buurt.gemeentecode, self.context['gem_gemeente_code'])
        self.assertEquals(buurt.wijkcode, self.context['wijk_wijk_code'])
        self.assertEquals(buurt.datum_begin_geldigheid_buurt, self.context['ingangsdatum_object'])
        self.assertEquals(buurt.datum_einde_geldigheid_buurt, self.context['einddatum_object'])

    def test_zakobj_enkelvoudig_document(self):
        pass

    def test_zaakobject_gemeente(self):
        pass

    def test_zaakobject_gemeentelijkeOpenbareRuimte(self):
        # TODO: Implement
        pass

    def test_zaakobject_huishouden(self):
        # TODO: Implement
        pass

    def test_zaakobject_inrichtingselement(self):
        # TODO: Implement
        pass

    def test_zaakobject_kadastraleOnroerendeZaak(self):
        self.context.update(**{
            'kadastrale_identificatie': '1234567',
            'kadastrale_gemeentecode': '12',
            'kadastrale_sectie': '34',
            'kadastraal_perceelnummer': '56',
            'apr_appartements_index': '78',
            'genereerbesluitident_identificatie_2': '123',
            'genereerzaakident_identificatie_2': self.genereerID(10),
            'ingangsdatum_object': '20170902',
        })
        vraag = 'creeerZaak_ZakLk01_koz.xml'
        response = self._do_request(self.porttype, vraag, self.context)

        zaak = Zaak.objects.get()
        self.assertEquals(zaak.zaakobject_set.count(), 1)
        zaakobj = zaak.zaakobject_set.get()
        self.assertEquals(zaakobj.relatieomschrijving, 'omschrijving')
        obj = zaakobj.object
        koz = obj.is_type()
        self.assertIs(type(koz), KadastraalPerceelObject)
        self.assertEquals(koz.identificatie, self.context['kadastrale_identificatie'])

        self.assertEquals(koz.kadastrale_aanduiding.kadastralegemeentecode, self.context['kadastrale_gemeentecode'])
        self.assertEquals(koz.kadastrale_aanduiding.sectie, self.context['kadastrale_sectie'])
        self.assertEquals(koz.kadastrale_aanduiding.perceelnummer, int(self.context['kadastraal_perceelnummer']))
        self.assertEquals(koz.kadastrale_aanduiding.appartementsrechtvolgnummer, int(self.context['apr_appartements_index']))

    def test_zaakobject_kunstwerkdeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_maatschappelijkeActiviteit(self):
        # TODO: Implement
        pass

    def test_zaakobject_medewerker(self):
        # TODO: Implement
        pass

    def test_zaakobject_natuurlijkPersoon(self):
        # TODO: Implement
        pass

    def test_zaakobject_nietNatuurlijkPersoon(self):
        # TODO: Implement
        pass

    def test_zaakobject_openbareRuimte(self):
        # TODO: Implement
        pass

    def test_zaakobject_organisatorischeEenheid(self):
        # TODO: Implement
        pass

    def test_zaakobject_pand(self):
        # TODO: Implement
        pass

    def test_zaakobject_samengesteldDocument(self):
        # TODO: Implement
        pass

    def test_zaakobject_spoorbaandeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_status(self):
        # TODO: Implement
        pass

    def test_zaakobject_terreindeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_vestiging(self):
        # TODO: Implement
        pass

    def test_zaakobject_waterdeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_wegdeel(self):
        # TODO: Implement
        pass

    def test_zaakobject_wijk(self):
        # TODO: Implement
        pass

    def test_zaakobject_woonplaats(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozDeelobject(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozObject(self):
        # TODO: Implement
        pass

    def test_zaakobject_wozWaarde(self):
        # TODO: Implement
        pass

    def test_zaakobject_zakelijkRecht(self):
        # TODO: Implement
        pass


class STPcreeerZaak_ZakLk01Tests(BaseTestPlatformTests):
    test_files_subfolder = 'stp_creeerZaak'
    porttype = 'OntvangAsynchroon'

    def setUp(self):
        super().setUp()

        # medewerker wordt geidentificeerd in de .xml bestanden, met
        # '${gemeentecode}56789' wat is vervangen door '0123456789'
        self.medewerker = MedewerkerFactory.create(
            organisatorische_eenheid__organisatieeenheididentificatie='01234',
            medewerkeridentificatie='56789')
        self.assertEqual(self.medewerker.identificatie, '0123456789')

        self.zaak_type = ZaakTypeFactory.create(
            zaaktypeomschrijving='Aanvraag burgerservicenummer behandelen',
            zaaktypeidentificatie='12345678')

        self.context = {
            'gemeentecode': '',
            'referentienummer': self.genereerID(10),

            'datumVandaag': self.genereerdatum(),
            'datumEergisteren': self.genereerdatum(-2),
            'tijdstipRegistratie': self.genereerdatumtijd(),

            'zds_zaaktype_omschrijving': 'Aanvraag burgerservicenummer behandelen',
            'zds_zaaktype_code': '12345678',
        }

    def _test_response(self, response):
        self.assertEquals(response.status_code, 200, response.content)

        response_root = etree.fromstring(response.content)
        response_berichtcode = response_root.xpath(
            '//stuf:stuurgegevens/stuf:berichtcode', namespaces=self.nsmap
        )[0].text
        self.assertEqual(response_berichtcode, BerichtcodeChoices.bv03, response.content)

    def test_create_01(self):
        """
        creeerZaak_zakLk01 volgnummer 1
        """
        self.assertFalse(Zaak.objects.exists())

        vraag = 'creeerZaak_ZakLk01_01.xml'
        self.context.update(**{
            'genereerbesluitident_identificatie_2': '123',
            'genereerzaakident_identificatie_2': self.genereerID(10),
        })
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

        # And now we are supposed to wait for the async processing, but since it is
        # not implemented we can immediately check.

        self.assertTrue(Zaak.objects.exists())
        expected = {
            'zaakidentificatie': self.context['genereerzaakident_identificatie_2'],
            'bronorganisatie': 1,
            'archiefstatus': 'Gearchiveerd',
            'verantwoordelijke_organisatie': 1,
            'omschrijving': 'omschrijving',
            'startdatum': self.context['datumVandaag'],
            'registratiedatum': self.context['datumVandaag'],
            'zaaktype_id': self.zaak_type.pk,
        }
        self.assertTrue(Zaak.objects.filter(**expected).exists())
        zaak = Zaak.objects.get(**expected)
        self.assertTrue(Rol.objects.filter(zaak=zaak, betrokkene=self.medewerker).exists())

    def test_create_03(self):
        """
        creeerZaak_zakLk01 volgnummer 3
        """
        vraag = 'creeerZaak_ZakLk01_03.xml'
        medewerker = MedewerkerFactory.create(
            medewerkeridentificatie='7007',
            organisatorische_eenheid=None,
        )
        self.assertEqual(medewerker.identificatie, '7007')

        ZaakTypeFactory.create(
            zaaktypeomschrijving='Aanvraag burgerservicenummer behandelen',
            zaaktypeidentificatie='12345679')

        # TODO: [TECH] This should be created in the tests, but the matching-data mismatches
        # with the required information. This can be removed once Issue #250 is solved.
        OrganisatorischeEenheidFactory.create(
            identificatie='1234987654',
            organisatieeenheididentificatie='1234987654',
            organisatieidentificatie='1234'
        )

        self.assertEquals(OverigeAdresseerbaarObjectAanduidingObject.objects.count(), 0)

        # In the test this is a 'T', however, the required field 'datum_begin_geldigheid_adresseerbaar_object_aanduiding'
        # isn't given a value in the StUF test, so we can't possibly create the OverigeAdresseerbaarObjectAanduidingObject object.OverigeAdresseerbaarObjectAanduidingObject
        # I assume, that the KING test suite assumes that we create this object in our database.
        OverigeAdresseerbaarObjectAanduidingObjectFactory.create(
            identificatie='0123456789101112',
            woonplaatsnaam='woonplaatsNaam',
            naam_openbare_ruimte='openbareRuimteNaam',
            huisnummer=99999,
            huisletter='A',
            huisnummertoevoeging='',
        )

        self.context.update(**{
            'genereerzaakident_identificatie_4': self.genereerID(10),
            'genereerbesluitident_identificatie_2': '123',
            'genereerzaakident_identificatie_2': self.genereerID(10),
        })
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

        self.assertEquals(Zaak.objects.count(), 1)
        expected = {
            'zaakidentificatie': self.context['genereerzaakident_identificatie_4'],
            'bronorganisatie': 1,
            'archiefstatus': 'Gearchiveerd',
            'verantwoordelijke_organisatie': 1,
            'omschrijving': 'omschrijving',
            'toelichting': 'toelichting',
            'startdatum': self.context['datumVandaag'],
            'registratiedatum': self.context['datumVandaag'],
            'publicatiedatum': self.context['datumVandaag'],
            'einddatum_gepland': self.context['datumVandaag'],
            'uiterlijke_einddatum_afdoening': self.context['datumVandaag'],
            'einddatum': self.context['datumVandaag'],
            'betalingsindicatie': '(Nog) niet',
            'laatste_betaaldatum': self.context['datumVandaag'],
            'archiefnominatie': 'Vernietigen',
            'zaaktype_id': self.zaak_type.pk,
        }
        self.assertTrue(Zaak.objects.filter(**expected).exists())
        zaak = Zaak.objects.get()

        self.assertEquals(zaak.zaakkenmerk_set.filter(
            kenmerk='kenmerk', kenmerk_bron='bron'
        ).count(), 2)

        self.assertEquals(zaak.anderzaakobject_set.filter(
            ander_zaakobject_omschrijving='omschrijving', ander_zaakobject_aanduiding='aanduiding',
            ander_zaakobject_registratie='registratie',
            ander_zaakobject_lokatie__startswith='<gml:OrientableSurface',
        ).count(), 2)

        self.assertEquals(zaak.zaakopschorting_set.filter(
            indicatie_opschorting='N', reden_opschorting='reden',
        ).count(), 1)

        self.assertEquals(zaak.zaakverlenging_set.filter(
            duur_verlenging=123, reden_verlenging='reden',
        ).count(), 1)

        expected = {
            'postadres_postcode': '1000',
            'woonplaatsnaam': 'woonplaatsNaam',
        }
        self.assertEquals(PostAdres.objects.filter(**expected).count(), 2)

        self.assertEquals(zaak.zaakobject_set.count(), 1)
        zaakobj = zaak.zaakobject_set.get()
        self.assertEquals(zaakobj.relatieomschrijving, 'omschrijving')
        obj = zaakobj.object
        adres = obj.is_type()
        self.assertEquals(adres.identificatie, '0123456789101112')
        self.assertEquals(adres.woonplaatsnaam, 'woonplaatsNaam')
        self.assertEquals(adres.naam_openbare_ruimte, 'openbareRuimteNaam')
        self.assertEquals(adres.huisnummer, 99999)
        self.assertEquals(adres.huisletter, 'A')
        self.assertEquals(adres.huisnummertoevoeging, '')

    @skip("fails on '<gerelateerde>', also lots of TODO's in the xml test file")
    def test_create_05(self):
        vraag = 'creeerZaak_ZakLk01_05.xml'
        self.context.update(
            genereerzaakident_identificatie_6=self.genereerID(10)
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

    @skip("several 'Dit veld mag niet leeg zijn' errors, also several TODO's in the xml test file ")
    def test_create_07(self):
        vraag = 'creeerZaak_ZakLk01_07.xml'
        self.context.update(
            creerzaak_identificatie_7=self.genereerID(10)
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

    @skip("several 'Dit veld mag niet leeg zijn' errors, also several TODO's in the xml test file ")
    def test_create_09(self):
        # VestigingFactory.create() ?

        vraag = 'creeerZaak_ZakLk01_09.xml'
        self.context.update(
            creerzaak_identificatie_9=self.genereerID(10)
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

    @skip("several 'Dit veld mag niet leeg zijn' errors, also several TODO's in the xml test file ")
    def test_create_11(self):
        vraag = 'creeerZaak_ZakLk01_11.xml'
        self.context.update(
            creerzaak_identificatie_11=self.genereerID(10)
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)

    # fails also datumVernietigingDossier, heeftAlsGemachtigde, heeftAlsUitvoerende,
    # heeftAlsVerantwoordelijke, heeftAlsOverigBetrokkene
    @skip("several 'Dit veld mag niet leeg zijn' errors, also several TODO's in the xml test file ")
    def test_create_13(self):
        vraag = 'creeerZaak_ZakLk01_13.xml'
        self.context.update(
            creerzaak_identificatie_13=self.genereerID(10)
        )
        response = self._do_request(self.porttype, vraag, self.context)

        self._test_response(response)


class creeerZaak_ZakLk01RegressionTests(BaseTestPlatformTests):
    test_files_subfolder = 'maykin_creeerZaak'
    porttype = 'OntvangAsynchroon'

    @skip('Pending resolve')
    def test_required_fields_in_datamodel(self):
        """
        See: https://taiga.maykinmedia.nl/project/haarlem-zaakmagazijn/issue/277
        """
        zaak_type = ZaakTypeFactory.create(
            zaaktypeomschrijving='MOR',
            zaaktypeidentificatie='1')

        org_eenheid = OrganisatorischeEenheidFactory.create(
            organisatieeenheididentificatie='DVV/KCC')

        vraag = 'creeerZaak_ZakLk01_taiga277.xml'
        response = self._do_request(self.porttype, vraag)

        self.assertEquals(response.status_code, 200, response.content)

    def test_naam_matching_query_does_not_exist(self):
        """
        See: https://taiga.maykinmedia.nl/project/haarlem-zaakmagazijn/issue/281
        """
        zaak_type = ZaakTypeFactory.create(
            zaaktypeomschrijving='MOR',
            zaaktypeidentificatie='1')

        org_eenheid = OrganisatorischeEenheidFactory.create(
            organisatieeenheididentificatie='DVV/KCC')

        vraag = 'creeerZaak_ZakLk01_taiga281.xml'
        response = self._do_request(self.porttype, vraag)

        self.assertEquals(response.status_code, 200, response.content)