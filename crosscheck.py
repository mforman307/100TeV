
def makehist(file, name):
    import ROOT
    from ROOT import TGraph,TCanvas,TH1F,TH2F,TFile,THStack,TLegend,gStyle ,TLatex
    f = ROOT.TFile.Open(file)
    tree = f.Get("OutputTree")
    roc_eff_dr = open('roceffdr_%s.txt'%(name),'w+')
    roc_rej_dr = open('rocrejdr_%s.txt'%(name),'w+')
    roc_eff_inv = open('roceffinv_%s.txt'%(name),'w+')
    rej = open('rejinv_%s.txt'%(name),'w+')
    roc_rej_inv = open('rocrejinv_%s.txt'%(name),'w+')
    all_hist = ROOT.TH1F("all_hist_%s"%(name), "all", 100, 0, 10)
    gen_hist = ROOT.TH1F("gen_hist_%s"%(name), "generated", 100, 0, 10)
    tag_hist = ROOT.TH1F("tag_hist_%s"%(name), "taggable", 100, 0, 10)
    sel_hist = ROOT.TH1F("sel_hist_%s"%(name), "selected", 100, 0, 10)
    fake_hist = ROOT.TH1F("fake_hist_%s"%(name), "faked", 100, 0, 10)
    dr_mu_top = ROOT.TH1F("dr_mu_top_%s"%(name), "mu_closesttop_dr", 50, 0, 0.4)
    inv_mass_all = ROOT.TH1F("inv_mass_all_%s"%(name), "invariant_mass_all", 100, 0, 1000)
    inv_mass_gen = ROOT.TH1F("inv_mass_gen_%s"%(name), "invariant_mass_gen", 100, 0, 1000)
    inv_mass_sel = ROOT.TH1F("inv_mass_sel_%s"%(name), "invariant_mass_sel", 100, 0, 1000)
    inv_mass_tag = ROOT.TH1F("inv_mass_tag_%s"%(name), "invariant_mass_tag", 100, 0, 1000)
    inv_mass_fake = ROOT.TH1F("inv_mass_fake_%s"%(name), "invariant_mass_fake", 100, 0, 1000)
    HT_all = ROOT.TH1F("ht_all_%s"%(name), "HT_all", 200, 0, 20000)
    HT_gen = ROOT.TH1F("ht_gen_%s"%(name), "HT_gen", 200, 0, 20000)
    HT_sel = ROOT.TH1F("ht_sel_%s"%(name), "HT_sel", 200, 0, 20000)
    HT_tag = ROOT.TH1F("ht_tag_%s"%(name), "HT_tag", 200, 0, 20000)
    HT_fake = ROOT.TH1F("ht_fake_%s"%(name), "HT_fake", 200, 0, 20000)
    HTjets_all = ROOT.TH1F("htjets_all_%s"%(name), "htjets_all", 200, 0, 20000)
    HTjets_gen = ROOT.TH1F("htjets_gen_%s"%(name), "htjets_gen", 200, 0, 20000)
    HTjets_sel = ROOT.TH1F("htjets_sel_%s"%(name), "htjets_sel", 200, 0, 20000)
    HTjets_tag = ROOT.TH1F("htjets_tag_%s"%(name), "htjets_tag", 200, 0, 20000)
    HTjets_fake = ROOT.TH1F("htjets_fake_%s"%(name), "htjets_fake", 200, 0, 20000)
    pt_mu_gen = ROOT.TH1F("pt_mu_gen_%s"%(name), "ptmuon_gen",100, 0, 10000)
    pt_mu_sel = ROOT.TH1F("pt_mu_sel_%s"%(name), "ptmuon_sel",100, 0, 10000)
    pt_mu_tag = ROOT.TH1F("pt_mu_tag_%s"%(name), "ptmuon_tag", 10, 0, 10000)
    pt_mu_fake = ROOT.TH1F("pt_mu_fake_%s"%(name), "ptmuon_fake",100, 0, 10000)
    pt_closestjet_gen = ROOT.TH1F("pt_jet_gen_%s"%(name), "ptclosestjet_gen",100, 0, 10000)
    pt_closestjet_sel = ROOT.TH1F("pt_jet_sel_%s"%(name), "ptclosestjet_sel",100, 0, 10000)
    pt_closestjet_tag = ROOT.TH1F("pt_jet_tag_%s"%(name), "ptclosestjet_tag",100, 0, 10000)
    pt_closestjet_fake = ROOT.TH1F("pt_jet_fake_%s"%(name), "ptclosestjet_fake",100, 0, 1000)
    ptmujet_ratio_gen = ROOT.TH1F("ptmujet_ratio_gen_%s"%(name), "ptmujet_ratio_gen",200, 0, 20)
    ptmujet_ratio_sel = ROOT.TH1F("ptmujet_ratio_sel_%s"%(name), "ptmujet_ratio_sel",200, 0, 20)
    ptmujet_ratio_tag = ROOT.TH1F("ptmujet_ratio_tag_%s"%(name), "ptmujet_ratio_tag",200, 0, 20)
    ptmujet_ratio_fake = ROOT.TH1F("ptmujet_ratio_fake_%s"%(name), "ptmujet_ratio_fake",200, 0, 20)
    inv_mass_dr = ROOT.TH2F("inv_mass_dr_%s"%(name), "inv_mass_dr", 100, 0, 10, 100, 0, 1000)
    all_hist.GetXaxis().SetTitle("DR")
    gen_hist.GetXaxis().SetTitle("DR")
    tag_hist.GetXaxis().SetTitle("DR")
    sel_hist.GetXaxis().SetTitle("DR")
    fake_hist.GetXaxis().SetTitle("DR")
    ratio = ROOT.TH1F("ratio_%s"%(name), "ratio", 10, 0, 5)
    if name == "tt":
	inv_mass_sel.SetLineColor(ROOT.kRed)
	sel_hist.SetLineColor(ROOT.kRed)
	HT_sel.SetLineColor(ROOT.kRed)
	pt_mu_sel.SetLineColor(ROOT.kRed)
    elif name == "QCD":
	sel_hist.SetLineColor(ROOT.kBlue)
	inv_mass_sel.SetLineColor(ROOT.kBlue)
	HT_sel.SetLineColor(ROOT.kBlue)
	pt_mu_sel.SetLineColor(ROOT.kBlue)
    print "scanning over %d events"%(tree.GetEntriesFast())
    event_cnt = 0
    N_gen=0
    N_sel = {}
    N_sel2 = {}
    inv_dict = {}
    dr_dict = {}
    eff_dict = {}
    for event in tree:
        event_cnt += 1
        if event_cnt%100==0:
            print "processed%d events"%(event_cnt)
        if event_cnt%10 != 0:
            continue
    
        lead = 0
        # initialize jet 4-Vector as first jet   
        
	jet_vec = ROOT.TLorentzVector()
        jet_vec.SetPtEtaPhiM(event.pTJet[0], event.etaJet[0], event.phiJet[0], 0)
        # create muon 4-Vector
        muon_vec = ROOT.TLorentzVector()
        ht = 0
        
        # to get hT, sum transverse momenta of first 10 jets 
        for j in range(0,10):
            ht += event.pTJet[j]
        HT_all.Fill(ht, event.weight)
        HTjets_all.Fill(event.HTjets, event.weight)
        n = 0

        # 4 TeV hT-jet requirement
        if ht > 4000:
            # loop over truth particles
       	    for i in range(0,50):
            #if truth particle is muon(Id=13), create 4-Vector for muon
                if abs(event.pdgIdTruth[i]) == 13:
                    muon_vec.SetPtEtaPhiM(event.pTTruth[i], event.etaTruth[i], event.phiTruth[i], .105)
                    # initialize closest jet as first jet
                    closest = jet_vec
                    N_gen+= event.weight
                    # loop over jets to find closest jet
                    for j in range(1,10):
                        jet = ROOT.TLorentzVector()
                        jet.SetPtEtaPhiM(event.pTJet[j], event.etaJet[j], event.phiJet[j], 0)
                        
                        # if jet less than previous in loop, set as closest
                        if muon_vec.DrEtaPhi(jet) < muon_vec.DrEtaPhi(closest):
                            closest = jet
                                #global closest_pt
                                # assign pT of closest jet 
                                #closest_pt = event.pTJet[j]
                                #print("jetpt:",closest_pt)
                        else:
                            continue
                    gen_hist.Fill(closest.DrEtaPhi(muon_vec), event.weight)
                    #print(closest.DrEtaPhi(muon_vec))
                    # Sum 4 Vectors of muon and jet
                    muon_jet = muon_vec + closest
                    pt_mu_gen.Fill(event.pTTruth[i], event.weight)
                    #pt_closestjet_gen.Fill(closest_pt, event.weight)

                    # create ratio of muon and jet pt
                    #if closest_pt != 0:
                        #ptmujet_ratio_gen.Fill(event.pTTruth[i]/closest_pt, event.weight)
                    
                    # fill ht of muon and jet once
                    if n < 1:
                        HT_gen.Fill(ht, event.weight)
                        HTjets_gen.Fill(event.HTjets, event.weight)
                        n += 1    
                    inv_mass_gen.Fill(muon_jet.M(), event.weight)
                    
                    # if muon has pt over 20 GeV, proceed to top search
                    # cut from 20 --> 0, cut at 20 reduces efficiency to ~70%
		    if event.pTTruth[i] > 20:
                        # initialize booleans
                        top = False
                        closest_top = None
                        m = 0
                        l = 0
                    # loop over truth particles, if top(Id=6) make 4-Vector
                        for j in range(1,50):
                            if abs(event.pdgIdTruth[j]) == 6:
                                particle2 = ROOT.TLorentzVector()
                                particle2.SetPtEtaPhiM(event.pTTruth[j], event.etaTruth[j], event.phiTruth[j], 172)
                                if closest_top==None or muon_vec.DrEtaPhi(particle2) < muon_vec.DrEtaPhi(closest_top):
                                    closest_top = particle2
                                else:
                                    continue

                        top = (closest_top != None)
                            
                        if top:
                	    dr_mu_top.Fill(closest_top.DrEtaPhi(muon_vec), event.weight)
                        
                        # fill the tag hists if there is a top and it's close to the jet nearest the muon
                        if top and closest.DrEtaPhi(closest_top) < 1:
                        	tag_hist.Fill(closest.DrEtaPhi(muon_vec), event.weight)
                                inv_mass_tag.Fill(muon_jet.M(), event.weight)
                                pt_mu_tag.Fill(event.pTTruth[j], event.weight)
                                    #pt_closestjet_tag.Fill(closest_pt, event.weight)
                                #if closest_pt != 0:
                                    #ptmujet_ratio_tag.Fill(event.pTTruth[i]/closest_pt, event.weight)
                         	if m < 1:
                                	HT_tag.Fill(ht, event.weight)
                                        HTjets_tag.Fill(event.HTjets, event.weight)

                                        m += 1

                            # fill the sel hists if the selection cut is passed
                            # muon is within 1 of closest jet
                            # changed cut from dr=1 to dr=0.3
                        if closest.DrEtaPhi(muon_vec) < 0.4:
                        	sel_hist.Fill(closest.DrEtaPhi(muon_vec), event.weight)
                                        #N_sel1+=1
                                        #print("N_sel1:%f"%(N_sel1))
                                inv_mass_dr.Fill(closest.DrEtaPhi(muon_vec), muon_jet.M())
                                inv_mass_sel.Fill(muon_jet.M(), event.weight)
					
                                pt_mu_sel.Fill(event.pTTruth[j], event.weight)
                                #pt_closestjet_sel.Fill(closest_pt, event.weight)
                                #if closest_pt != 0:
                                	#ptmujet_ratio_sel.Fill(event.pTTruth[i]/closest_pt, event.weight)
                                if l < 1:
                                	HT_sel.Fill(ht, event.weight)
                                        HTjets_sel.Fill(event.HTjets, event.weight)
                                        l += 1

        	        dr = closest.DrEtaPhi(muon_vec)       
                       	nbins = 1000
                        xmax = 4.0
			invmax = 500.0
     	                for n in xrange(1,nbins):
				inv_cut = n*(invmax/nbins)
                               	dr_cut = n*(xmax/nbins)
                       		if dr < dr_cut:
					N_sel[n]=N_sel.get(n, 0) + event.weight
			       		dr_dict[n]=dr_dict.get(n, dr_cut)	
            		       	if muon_jet.M() < inv_cut and dr < dr_cut:
 					N_sel2[n] = N_sel2.get(n, 0) + event.weight
		              	     	inv_dict[n] = inv_dict.get(n, inv_cut) 
			        
                        # fake hist if there is no top or dr of closest jet and closest top are greater than 1   
                        if not top or closest.DrEtaPhi(closest_top) > 1:   
                            fake_hist.Fill(closest.DrEtaPhi(muon_vec), event.weight)
                            inv_mass_fake.Fill(muon_jet.M(), event.weight)
                            HT_fake.Fill(ht, event.weight)
                            HTjets_fake.Fill(event.HTjets, event.weight)
                            pt_mu_fake.Fill(event.pTTruth[j], event.weight)
                            #pt_closestjet_fake.Fill(closest_pt, event.weight)
                            #if closest_pt != 0:
                                #ptmujet_ratio_fake.Fill(event.pTTruth[i]/closest_pt, event.weight)

    #for value in N_sel.values():
	#eff.append(((float(value))/(float(N_gen))))
	#roc_eff_dr.write("%f"%(((float(value))/(float(N_gen)))))
	#roc_eff_dr.write(',')
        #roc_rej_dr.write("%f"%((1-((float(value))/(float(N_gen))))))
	#roc_rej_dr.write(',')
    #for value in N_sel2.values():
	#roc_eff_inv.write("%f"%(((float(value))/(float(N_gen)))))
	#roc_eff_inv.write(',')
        #rej.write("%f"%((1-((float(value))/(float(N_gen))))))
	#rej.write(',')
    print(N_sel2)
    print(N_sel)
    for i in xrange(1,1000):
    	val1 = N_sel2[i] if i in N_sel2 else 0
	val2 = N_sel[i] if i in N_sel else 0
	if val1 and val2 != 0:
		roc_eff_inv.write("%f"%((float(val1))/(float(val2))))
		roc_eff_inv.write(',')
		rej.write("%f"%(1-((float(val1))/(float(val2)))))
		rej.write(',')
    #roc_eff_dr.close()
    #roc_rej_dr.close()
    roc_eff_inv.close()
    rej.close()
    for bin in range(1, sel_hist.GetNbinsX()):
        if gen_hist.GetBinContent(bin) <= 0:
            ratio.SetBinContent(bin, 0)
        else:
            ratio.SetBinContent(bin,sel_hist.GetBinContent(bin)/gen_hist.GetBinContent(bin))

    check_file = ROOT.TFile("crosscheck.root", "UPDATE")
    ratio.Draw()
    #all_hist.Draw()
    fake_hist.Draw()
    gen_hist.Draw()
    tag_hist.Draw()
    sel_hist.Draw()
    HT_all.Draw()
    HT_gen.Draw()
    HT_sel.Draw()
    HT_tag.Draw()
    HT_fake.Draw()
    dr_mu_top.Draw()
    
    inv_mass_gen.Draw()
    inv_mass_sel.Draw()
    inv_mass_tag.Draw()
    inv_mass_fake.Draw()
    HTjets_all.Draw()
    HTjets_gen.Draw()
    HTjets_sel.Draw()
    HTjets_tag.Draw()
    HTjets_fake.Draw()
    pt_mu_gen.Draw()
    pt_mu_sel.Draw()
    pt_mu_tag.Draw()
    pt_mu_fake.Draw()
    pt_closestjet_gen.Draw()
    pt_closestjet_sel.Draw()
    pt_closestjet_tag.Draw()
    pt_closestjet_fake.Draw()
    ptmujet_ratio_gen.Draw()
    ptmujet_ratio_sel.Draw()
    ptmujet_ratio_tag.Draw()
    ptmujet_ratio_fake.Draw()
    inv_mass_dr.Draw("colz")
    
    
    HT_all.Write()
    HT_gen.Write()
    HT_sel.Write()
    HT_tag.Write()
    HT_fake.Write()
    
    
    #inv_mass_all.Write()
    inv_mass_gen.Write()
    inv_mass_sel.Write()
    inv_mass_tag.Write()
    inv_mass_fake.Write()
    
    HTjets_all.Write()
    HTjets_gen.Write()
    HTjets_sel.Write()
    HTjets_tag.Write()
    HTjets_fake.Write()

    #all_hist.Write()
    gen_hist.Write()
    tag_hist.Write()
    sel_hist.Write()
    fake_hist.Write()
    ratio.Write()
    
    pt_mu_gen.Write()
    pt_mu_sel.Write()
    pt_mu_tag.Write()
    pt_mu_fake.Write()
    pt_closestjet_gen.Write()
    pt_closestjet_sel.Write()
    pt_closestjet_tag.Write()
    pt_closestjet_fake.Write()
    ptmujet_ratio_gen.Write()
    ptmujet_ratio_sel.Write()
    ptmujet_ratio_tag.Write()
    ptmujet_ratio_fake.Write()
    dr_mu_top.Write()
    inv_mass_dr.Write()

    check_file.Close()
#tt
makehist("/export/home/mhance/FCC/Snowmass/DelphesReader/output/backgrounds_100TeV/delphes.tt-4p_100TEV.NoPileUp.root", "tt")
#ttB
#makehist("/export/home/mhance/FCC/Snowmass/DelphesReader/output/backgrounds_100TeV/delphes.ttB-4p_100TEV.NoPileUp.root", "ttB")
#QCD
makehist("/export/home/mhance/FCC/Snowmass/DelphesReader/output/backgrounds_100TeV/delphes.bb-4p_100TEV.NoPileUp.root", "QCD")
#makehist("/export/home/mhance/FCC/Snowmass/DelphesReader/output/GO_decoupledSQ_100TeV_LHE_TTALL/delphes.GO_decoupledSQ_100TeV_LHE_TTALL.NoPileUp.GO11944.tt.N00001_100TEV.root", "ttsignal")


                             
                
   
