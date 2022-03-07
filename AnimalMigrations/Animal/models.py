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
    species_name = models.CharField(max_length=50,)
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
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.taxonomy_domain = 'Eucariota'
        self.taxonomy_kingdom = 'Animalia'
        self.taxonomy_phylum = 'Chordata'
        self.taxonomy_class = 'Amphibia'


class Frog(Amphibia):
    TAX_SPECIES_OPTIONS = {
        'Kumak nizinny': 'Bombina bombina',
        'Kumak górski': 'Bombina variegata',
        'Grzebiuszka ziemna': 'Pelobates fuscus',
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
        'Żaba trawna': 'Rana temporaria',
    }

    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.taxonomy_order = 'Anura'
        self.taxonomy_family = 'Ranidae'
        self.taxonomy_genus = 'Rana'

        self.species_name = models.CharField(max_length=50, choices=Frog.TAX_SPECIES_OPTIONS)