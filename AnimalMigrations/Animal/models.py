from django.db import models


class Animal(models.Model):
    PROTECTION_STATUS_OPTIONS = {
        'EX': 'Extinct',
        'EW': 'Extinct in the wild',
        'CR': 'Critically endangered',
        'EN': 'Endangered',
        'VU': 'Vulnerable',
        'NT': 'Near threatened',
        'CD': 'Conservation dependent',
        'LC': 'Least concern',
        'DO': 'Domesticated',
        'DD': 'Data deficient',
        'NE': 'Not evaluated',
    }
    latin_name = models.CharField(max_length=100, unique=True, choices='')
    species_name = models.CharField(max_length=50, choices="")
    taxonomy_domain = models.CharField(max_length=50, choices="")
    taxonomy_kingdom = models.CharField(max_length=50, choices="")
    taxonomy_phylum = models.CharField(max_length=50, choices="")
    taxonomy_class = models.CharField(max_length=50, choices="")
    taxonomy_order = models.CharField(max_length=50, choices="")
    taxonomy_family = models.CharField(max_length=50, choices="")
    taxonomy_genus = models.CharField(max_length=50, choices="")
    protection_status = models.CharField(max_length=50, choices=PROTECTION_STATUS_OPTIONS)
    notes = models.TextField(max_length=400)
    event = models.ManyToManyField('Event')
    location = models.ManyToManyField('Location')


class Amphibia(Animal):
    TAX_DOMAIN_OPTIONS = ['Eucariota']
    TAX_KINGDOM_OPTIONS = ['Animalia']
    TAX_PHYLUM_OPTIONS = ['Chordata']
    TAX_CLASS_OPTIONS = ['Amphibia']
    TAX_ORDER_OPTIONS = ['Anura']
    TAX_FAMILY_OPTIONS = ['Ranidae']
    TAX_GENUS_OPTIONS = ['Rana']

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.taxonomy_domain = models.CharField(max_length=50, choices=Amphibia.TAX_DOMAIN_OPTIONS)
        self.taxonomy_kingdom = models.CharField(max_length=50, choices=Amphibia.TAX_KINGDOM_OPTIONS)
        self.taxonomy_phylum = models.CharField(max_length=50, choices=Amphibia.TAX_PHYLUM_OPTIONS)
        self.taxonomy_class = models.CharField(max_length=50, choices=Amphibia.TAX_CLASS_OPTIONS)
        self.taxonomy_order = models.CharField(max_length=50, choices=Amphibia.TAX_ORDER_OPTIONS)
        self.taxonomy_family = models.CharField(max_length=50, choices=Amphibia.TAX_FAMILY_OPTIONS)
        self.taxonomy_genus = models.CharField(max_length=50, choices=Amphibia.TAX_GENUS_OPTIONS)


class Frogs(Amphibia):
    TAX_SPECIES_OPTIONS = {
        'Kumak nizinny': 'Bombina bombina',
        'Kumak górski': 'Bombina variegata',
        'Grzebiuszka ziemna': 'Pelobates     fuscus',
        'Ropucha szara': 'Bufo bufo',
        'Ropucha paskówka': 'Epidalea calamita, syn. Bufo calamita',
        'Ropucha zielona': 'Bufotes viridis, syn. Pseudepidalea viridis, Bufo viridis',
        'Rzekotka drzewna': 'Hyla arborea',
        'Rzekotka wschodnia': 'Hyla orientalis',
        'Żaba wodna': 'Pelophylax kl.esculentus, syn.Rana esculenta',
        'Żaba jeziorkowa': 'Pelophylax lessonae syn.Rana lessonae',
        'Żaba śmieszka': 'Pelophylax ridibundus syn.Rana ridibunda',
        'Żaba moczarowa': 'Rana arvalis',
        'Żaba zwinka': 'Rana dalmatina',
        'Żaba trawna': 'Rana temporaria ',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.latin_name = models.CharField(max_length=100, unique=True, choices=Frogs.TAX_SPECIES_OPTIONS.keys)
        self.species_name = models.CharField(max_length=50, choices=Frogs.TAX_SPECIES_OPTIONS.values)