from negocio_fechado.models import Offer, Tender

class OfferService:
    def accept_tender(offer_pk, tender_pk):
        offer = Offer.objects.get(pk=offer_pk)
        tender = Tender.objects.get(pk=tender_pk)

        offer.state = 2
        tender.state = 2

        offer.save()
        tender.save()
        
        # recuse another tenders
        another_tenders = Tender.objects.filter(offer__pk=offer_pk).exclude(pk=tender_pk)
        for t in another_tenders:
            t.state = 3
            t.save()
            