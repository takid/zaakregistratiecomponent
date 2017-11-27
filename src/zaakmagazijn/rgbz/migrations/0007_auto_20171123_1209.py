# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-23 11:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import zaakmagazijn.rgbz.validators
import zaakmagazijn.utils.fields
import zaakmagazijn.utils.stuf_datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rgbz', '0006_recreate-vzo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='naam',
            name='voorvoegsel_geslachtsnaam',
        ),
        migrations.RemoveField(
            model_name='natuurlijkpersoon',
            name='naam',
        ),
        migrations.RemoveField(
            model_name='natuurlijkpersoon',
            name='naam_aanschrijving',
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_aanschrijving_aanhef_aanschrijving',
            field=models.CharField(blank=True, help_text='De aanhef waarmee de persoon aangeschreven wil worden.', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_aanschrijving_geslachtsnaam_aanschrijving',
            field=models.CharField(blank=True, help_text='Geslachtsnaam die de persoon wenst te voeren', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_aanschrijving_voorletters_aanschrijving',
            field=models.CharField(blank=True, help_text='De voorletters waarmee een persoon aangeschreven wil worden.', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_aanschrijving_voornamen_aanschrijving',
            field=models.CharField(blank=True, help_text='Voornamen bij de naam die de persoon wenst te voeren.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_adelijke_titel',
            field=models.CharField(blank=True, choices=[('B', 'Baron'), ('B', 'Barones'), ('G', 'Graaf'), ('G', 'Gravin'), ('H', 'Hertog'), ('H', 'Hertogin'), ('M', 'Markies'), ('M', 'Markiezin'), ('P', 'Prins'), ('P', 'Prinses'), ('R', 'Ridder')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_geslachtsnaam',
            field=models.CharField(default='-', help_text='De stam van de geslachtsnaam.', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_voornamen',
            field=models.CharField(blank=True, help_text='Voornamen bij de naam die de persoon wenst te voeren.', max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='natuurlijkpersoon',
            name='naam_voorvoegsel_geslachtsnaam_voorvoegsel',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AddField(
            model_name='overigeadresseerbaarobjectaanduidingobject',
            name='postcode',
            field=models.CharField(blank=True, max_length=7, null=True),
        ),
        migrations.AddField(
            model_name='rol',
            name='begin_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='rol',
            name='begin_relatie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='rol',
            name='eind_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='rol',
            name='eind_relatie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='rol',
            name='tijdstip_registratie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, default=zaakmagazijn.utils.stuf_datetime.now, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='zaak',
            name='_deelzaken_indicatie',
            field=models.CharField(choices=[('J', 'Ja'), ('N', 'Nee')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='zaak',
            name='begin_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='zaak',
            name='eind_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='zaak',
            name='tijdstip_registratie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, default=zaakmagazijn.utils.stuf_datetime.now, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='anderbuitenlandsnietnatuurlijkpersoonobject',
            name='datum_aanvang',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum van aanvang van de NIET-NATUURLIJK PERSOON', max_length=9),
        ),
        migrations.AlterField(
            model_name='appartementsrechtobject',
            name='datum_begin_geldigheid_kadastrale_onroerende_zaak',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, max_length=9),
        ),
        migrations.AlterField(
            model_name='besluit',
            name='tijdstip_registratie',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, default=zaakmagazijn.utils.stuf_datetime.now, max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='besluittype',
            name='datum_begin_geldigheid_besluittype',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, max_length=9),
        ),
        migrations.AlterField(
            model_name='buurtobject',
            name='datum_begin_geldigheid_buurt',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de buurt is gecreëerd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='gemeentelijkeopenbareruimteobject',
            name='datum_begin_geldigheid_gemeentelijke_openbare_ruimte',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de OPENBARE RUIMTE formeel is benoemd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='gemeenteobject',
            name='datum_begin_geldigheid_gemeente',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de gemeente is ontstaan', max_length=9),
        ),
        migrations.AlterField(
            model_name='huishoudenobject',
            name='datum_begin_geldigheid_huishouden',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het HUISHOUDEN is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='informatieobjecttype',
            name='datum_begin_geldigheid_informatieobjecttype',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, max_length=9),
        ),
        migrations.AlterField(
            model_name='ingeschrevennietnatuurlijkpersoonobject',
            name='datum_aanvang',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum van aanvang van de NIET-NATUURLIJK PERSOON', max_length=9),
        ),
        migrations.AlterField(
            model_name='ingeschrevennietnatuurlijkpersoonobject',
            name='rsin',
            field=models.CharField(help_text='Het door een kamer toegekend uniek nummer voor de INGESCHREVEN NIET-NATUURLIJK PERSOON', max_length=17),
        ),
        migrations.AlterField(
            model_name='inrichtingselementobject',
            name='datum_begin_geldigheid_inrichtingselement',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het inrichtingselement is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='kadastraalperceelobject',
            name='datum_begin_geldigheid_kadastrale_onroerende_zaak',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de gegevens van de kadastrale onroerende zaak voor het eerst geldig zijn geworden.', max_length=9),
        ),
        migrations.AlterField(
            model_name='kunstwerkdeelobject',
            name='datum_begin_geldigheid_kunstwerkdeel',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het kunstwerkdeel is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='ligplaatsobject',
            name='datum_begin_geldigheid_benoemd_terrein',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop van gemeentewege het benoemd terrein formeel is aangewezen.', max_length=9),
        ),
        migrations.AlterField(
            model_name='natuurlijkpersoon',
            name='burgerservicenummer',
            field=models.CharField(blank=True, help_text='Het burgerservicenummer, bedoeld in artikel 1.1 van de Wet algemene bepalingen burgerservicenummer.', max_length=9, null=True, validators=[zaakmagazijn.rgbz.validators.validate_non_negative_string]),
        ),
        migrations.AlterField(
            model_name='natuurlijkpersoon',
            name='nummer_ander_natuurlijk_persoon',
            field=models.CharField(blank=True, help_text='Het door de gemeente uitgegeven unieke nummer voor een ANDER NATUURLIJK PERSOON', max_length=17, null=True),
        ),
        migrations.AlterField(
            model_name='nietnatuurlijkpersoon',
            name='datum_aanvang',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum van aanvang van de NIET-NATUURLIJK PERSOON', max_length=9),
        ),
        migrations.AlterField(
            model_name='nietnatuurlijkpersoon',
            name='rsin',
            field=models.CharField(help_text='Het door een kamer toegekend uniek nummer voor de INGESCHREVEN NIET-NATUURLIJK PERSOON', max_length=17),
        ),
        migrations.AlterField(
            model_name='nummeraanduidingobject',
            name='datum_begin_geldigheid_adresseerbaar_object_aanduiding',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de ADRESSEERBAAR OBJECT AANDUIDING formeel is vastgesteld.', max_length=9),
        ),
        migrations.AlterField(
            model_name='openbareruimteobject',
            name='datum_begin_geldigheid_openbare_ruimte',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de OPENBARE RUIMTE formeel is benoemd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='organisatorischeeenheid',
            name='datum_ontstaan',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de organisatorische eenheid is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='overigeadresseerbaarobjectaanduidingobject',
            name='datum_begin_geldigheid_adresseerbaar_object_aanduiding',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de ADRESSEERBAAR OBJECT AANDUIDING formeel is vastgesteld.', max_length=9),
        ),
        migrations.AlterField(
            model_name='overiggebouwdobject',
            name='datum_begin_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop vangeldigheid gebouwd gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een GEBOUWD OBJECT conform de vergunning, de melding of de aanschrijving zijn uitgevoerd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='overigterreinobject',
            name='datum_begin_geldigheid',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop van gemeentewege het benoemd terrein formeel is aangewezen.', max_length=9),
        ),
        migrations.AlterField(
            model_name='pandobject',
            name='datum_begin_geldigheid_pand',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop van gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een PAND conform de vergunning, de melding of de aanschrijving zijn uitgevoerd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='spoorbaandeelobject',
            name='datum_begin_geldigheid_spoorbaandeel',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het spoorbaandeel is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='standplaatsobject',
            name='datum_begin_geldigheid_benoemd_terrein',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop van gemeentewege het benoemd terrein formeel is aangewezen.', max_length=9),
        ),
        migrations.AlterField(
            model_name='statustype',
            name='datum_begin_geldigheid_statustype',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het STATUSTYPE is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='terreindeelobject',
            name='datum_begin_geldigheid_terreindeel',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het terreindeel is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='verblijfsobject',
            name='datum_begin_geldigheid_gebouwd_object',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='gemeentewege is vastgesteld dat de bouwwerkzaamheden betreffende de oprichting van een GEBOUWD OBJECT conform de vergunning, de melding of de aanschrijving zijn uitgevoerd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='vestiging',
            name='datum_aanvang',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum van aanvang van de vestiging.', max_length=9),
        ),
        migrations.AlterField(
            model_name='vestiging',
            name='locatieadres',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='locatieadres', to='rsgb.Locatieadres'),
        ),
        migrations.AlterField(
            model_name='waterdeelobject',
            name='datum_begin_geldigheid_waterdeel',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het waterdeel is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='wegdeelobject',
            name='datum_begin_geldigheid_wegdeel',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop het wegdeel is ontstaan', max_length=9),
        ),
        migrations.AlterField(
            model_name='wijkobject',
            name='datum_begin_geldigheid_wijk',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de wijk is gecreëerd.', max_length=9),
        ),
        migrations.AlterField(
            model_name='woonplaatsobject',
            name='datum_begin_geldigheid_woonplaats',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='De datum waarop de woonplaats is ontstaan', max_length=9),
        ),
        migrations.AlterField(
            model_name='wozdeelobject',
            name='datum_begin_geldigheid_deelobject',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='Een aanduiding op welk tijdstip een deelobject is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='wozobject',
            name='datum_begin_geldigheid_wozobject',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='Een aanduiding op welk tijdstip een object is ontstaan.', max_length=9),
        ),
        migrations.AlterField(
            model_name='zaak',
            name='laatste_betaaldatum',
            field=zaakmagazijn.utils.fields.StUFDateTimeField(blank=True, help_text='De datum waarop de meest recente betaling is verwerkt van kosten die gemoeid zijn met behandeling van de zaak.', max_length=18, null=True),
        ),
        migrations.AlterField(
            model_name='zaakinformatieobject',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='rgbz.Status'),
        ),
        migrations.AlterField(
            model_name='zaaktype',
            name='datum_begin_geldigheid_zaaktype',
            field=zaakmagazijn.utils.fields.StUFDateField(default=zaakmagazijn.utils.stuf_datetime.today, help_text='Datum begin geldigheid zaaktype', max_length=9),
        ),
    ]
