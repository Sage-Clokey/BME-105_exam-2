from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER

doc = SimpleDocTemplate(
    "/mnt/c/Users/SajcS/Desktop/BME-105_exam-2/BME105_Exam2_CheatSheet.pdf",
    pagesize=letter,
    leftMargin=0.5*inch, rightMargin=0.5*inch,
    topMargin=0.5*inch, bottomMargin=0.5*inch
)

styles = getSampleStyleSheet()

title_style = ParagraphStyle('Title', parent=styles['Normal'],
    fontSize=14, fontName='Helvetica-Bold', textColor=colors.HexColor('#1a1a5e'),
    spaceAfter=4, alignment=TA_CENTER)

h1_style = ParagraphStyle('H1', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica-Bold', textColor=colors.white,
    backColor=colors.HexColor('#1a1a5e'), spaceBefore=8, spaceAfter=3,
    leftIndent=4, rightIndent=4, borderPadding=3)

h2_style = ParagraphStyle('H2', parent=styles['Normal'],
    fontSize=8.5, fontName='Helvetica-Bold', textColor=colors.HexColor('#1a1a5e'),
    spaceBefore=5, spaceAfter=2)

body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=7.5, fontName='Helvetica', leading=10,
    spaceBefore=1, spaceAfter=1, leftIndent=8)

bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
    fontSize=7.5, fontName='Helvetica', leading=10,
    spaceBefore=0, spaceAfter=0, leftIndent=16, bulletIndent=8)

formula_style = ParagraphStyle('Formula', parent=styles['Normal'],
    fontSize=8, fontName='Helvetica-Bold', textColor=colors.HexColor('#8b0000'),
    backColor=colors.HexColor('#fff8f8'), spaceBefore=2, spaceAfter=2,
    leftIndent=10, borderPadding=2)

note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=7, fontName='Helvetica-Oblique', textColor=colors.HexColor('#555555'),
    leftIndent=10, spaceBefore=1)

def h1(text): return Paragraph(f"&nbsp;{text}", h1_style)
def h2(text): return Paragraph(text, h2_style)
def p(text): return Paragraph(text, body_style)
def b(text): return Paragraph(f"• {text}", bullet_style)
def formula(text): return Paragraph(text, formula_style)
def note(text): return Paragraph(f"<i>{text}</i>", note_style)
def sp(n=3): return Spacer(1, n)
def hr(): return HRFlowable(width="100%", thickness=0.5, color=colors.HexColor('#cccccc'))

story = []

story.append(Paragraph("BME 105 — Exam 2 Cheat Sheet", title_style))
story.append(Paragraph("Lectures 13–23 | Winter 2026", ParagraphStyle('sub', parent=styles['Normal'],
    fontSize=9, alignment=TA_CENTER, textColor=colors.HexColor('#555555'), spaceAfter=6)))
story.append(hr())
story.append(sp(4))

# ── SECTION 1: CALCULATIONS ──────────────────────────────────────────
story.append(h1("CALCULATIONS (show your work!)"))
story.append(sp())

story.append(h2("Hardy-Weinberg Equilibrium (Lec 20)"))
story.append(formula("p + q = 1     |     p² + 2pq + q² = 1"))
story.append(b("p = freq(dominant allele), q = freq(recessive allele)"))
story.append(b("p² = AA freq, 2pq = Aa freq, q² = aa freq"))
story.append(b("<b>5 Assumptions</b> (violation → not in HWE / evolution occurring):"))
story.append(p("&nbsp;&nbsp;&nbsp;Random mating · No mutation · No gene flow · No selection · Infinite pop size (no drift)"))
story.append(b("Steps: (1) get q from q² (affected), (2) get p = 1−q, (3) calculate 2pq for carriers"))
story.append(sp())

story.append(h2("Chi-Squared Test for HWE (Lec 20)"))
story.append(formula("χ² = Σ (Observed − Expected)² / Expected"))
story.append(b("df = # genotype classes − # alleles   (for biallelic: df = 1)"))
story.append(b("If χ² > critical value → reject HWE (population IS evolving)"))
story.append(sp())

story.append(h2("Natural Selection & Fitness (Lec 21)"))
story.append(formula("W = p²·w_AA + 2pq·w_Aa + q²·w_aa   (normalization factor)"))
story.append(formula("freq after selection: p'² = p²·w_AA / W,  2p'q' = 2pq·w_Aa / W, etc."))
story.append(b("Relative fitness: set highest fitness genotype = 1.0, scale others"))
story.append(b("Recessive deleterious allele: hidden in heterozygotes → slow removal (exponential decay of q²)"))
story.append(b("dN/dS ratio: >1 = positive selection, ~1 = neutral, <1 = purifying/stabilizing selection"))
story.append(b("<b>Mutation</b> = change in DNA sequence; <b>Substitution</b> = mutation fixed in population"))
story.append(sp())

story.append(h2("Genetic Drift & Founder Effect (Lec 20)"))
story.append(b("Drift = random allele freq change; larger effect in <b>small</b> populations"))
story.append(b("Allele fixation: freq reaches 1.0 (or 0) — lost/fixed by chance"))
story.append(b("Founder effect: small group founds new population → reduced diversity, high drift"))
story.append(sp(6))

# ── SECTION 2: EPIGENETICS ───────────────────────────────────────────
story.append(h1("EPIGENETICS (Lecs 14–15)"))
story.append(sp())

story.append(h2("Definition"))
story.append(p("Heritable alteration in gene expression <b>NOT</b> due to mutation in DNA sequence"))
story.append(sp())

story.append(h2("Chromatin-Level Regulation"))
data = [
    ['Mechanism', 'Effect', 'Key Detail'],
    ['DNA methylation (CpG)', 'Silences gene', 'Methylated C blocks transcription; unmethylated = active'],
    ['Histone acetylation', 'Opens chromatin (active)', 'Neutralizes + charge → loosens DNA–histone binding'],
    ['Histone methylation', 'Context-dependent', 'H3K4me3 = active; H3K27me3 = repressed'],
    ['Nucleosome positioning', 'Blocks/exposes DNA', 'Packed = heterochromatin; open = euchromatin'],
]
t = Table(data, colWidths=[1.5*inch, 1.8*inch, 3.2*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t)
story.append(sp())

story.append(h2("Transcriptional Regulation: cis vs. trans"))
story.append(b("<b>cis</b> (same chromosome/molecule): promoters, enhancers, insulators"))
story.append(b("<b>trans</b> (diffusible): transcription factors, activators/coactivators, repressors/corepressors"))
story.append(b("TFs can <b>activate OR repress</b> — depends on context/cofactors"))
story.append(b("Activators: recruit coactivators, remodel chromatin to open state"))
story.append(b("Repressors: recruit corepressors, compact chromatin"))
story.append(sp())

story.append(h2("Non-coding RNAs"))
story.append(b("Bind DNA reverse-complements → localize chromatin-modifying proteins"))
story.append(b("RNA-RNA binding important post-transcriptionally (e.g., RNAi)"))
story.append(sp())

story.append(h2("Sequencing Assays"))
data2 = [
    ['Assay', 'What it detects'],
    ['ChIP-seq', 'Protein–DNA interactions (TF binding sites, histone marks)'],
    ['ATAC-seq', 'Open chromatin regions (accessible DNA)'],
    ['Hi-C', '3D chromatin structure / chromosome contacts'],
    ['Bisulfite-seq', 'DNA methylation: unmethylated C→U; methylated C unchanged'],
    ['Nanopore/PacBio', 'Can detect methylation from raw signal (no bisulfite needed)'],
]
t2 = Table(data2, colWidths=[1.3*inch, 5.2*inch])
t2.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t2)
story.append(sp())

story.append(h2("Genomic Imprinting (Lec 15)"))
story.append(b("Only one parental allele expressed — determined by parent of origin"))
story.append(b("DNA methylation marks inherited through <b>mitosis</b>, rewritten during <b>meiosis</b>"))
story.append(b("Pedigree clue: trait passes through one sex only (e.g., always maternal)"))
story.append(b("Parental conflict hypothesis: paternal genes maximize offspring resource use; maternal genes moderate it"))
story.append(b("CpG islands: recruit methylation (at Cs) AND activators; activators block methylation → gene on"))
story.append(sp(6))

# ── SECTION 3: GWAS & QTL ────────────────────────────────────────────
story.append(h1("GWAS & QTL MAPPING (Lec 16)"))
story.append(sp())

data3 = [
    ['', 'GWAS', 'QTL Mapping'],
    ['Population', 'Large natural population', 'Controlled crosses (F2, RIL)'],
    ['Resolution', 'Coarse (haplotype blocks)', 'Fine-scale (recombinants)'],
    ['Linkage', 'High LD → associated SNP may not be causal', 'Recombination breaks LD → more precise'],
    ['Output', 'Associated SNP / region', 'Quantitative trait locus interval'],
]
t3 = Table(data3, colWidths=[1.2*inch, 2.7*inch, 2.6*inch])
t3.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('BACKGROUND', (0,1), (0,-1), colors.HexColor('#dde0f0')),
    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (1,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (1,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t3)
story.append(sp())
story.append(b("Key insight: associated SNP is in a <b>linked haplotype block</b> with the causal variant — not necessarily causal itself"))
story.append(b("Recombination breaks up LD → enables independent testing of alleles vs. phenotypes"))
story.append(b("eQTL: integrate gene expression with GWAS/QTL to identify regulatory variants"))
story.append(b("More genes → more continuous trait → smaller effect per locus"))
story.append(sp(6))

# ── SECTION 4: FORWARD/REVERSE GENETICS ─────────────────────────────
story.append(h1("FORWARD/REVERSE GENETICS & COMPLEMENTATION (Lec 13)"))
story.append(sp())
story.append(b("<b>Forward genetics</b>: start with phenotype → find the gene (e.g., mutagenesis screen)"))
story.append(b("<b>Reverse genetics</b>: start with gene → test effect on phenotype (e.g., CRISPR knockout)"))
story.append(sp())
story.append(h2("Complementation Test"))
story.append(b("Cross two homozygous recessive mutants; if offspring are <b>wild-type</b> → mutations in <b>different</b> genes"))
story.append(b("If offspring are <b>mutant</b> → same gene (fail to complement)"))
story.append(b("<b>Recombination is the limiting factor</b> for fine-scale mapping — more recombinants = better resolution"))
story.append(sp(6))

# ── SECTION 5: TRANSGENES / RNAi ────────────────────────────────────
story.append(h1("TRANSGENES, RNAi, REPORTERS (Lec 17)"))
story.append(sp())

story.append(h2("Delivery Methods"))
data4 = [
    ['Method', 'What it uses', 'Target'],
    ['Transfection / Transformation', 'DNA/RNA or plasmid; chemical/electroporation', 'Cells in culture'],
    ['Transduction', 'Viral vector (retrovirus, lentivirus, AAV)', 'Cells or organisms'],
    ['Conjugation', 'Direct cell–cell contact (plasmid transfer)', 'Bacteria'],
]
t4 = Table(data4, colWidths=[2.0*inch, 2.7*inch, 1.8*inch])
t4.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t4)
story.append(sp())

story.append(h2("Reporter Genes"))
story.append(b("Express a detectable product (GFP, luciferase, lacZ) under control of a promoter of interest"))
story.append(b("Used to: visualize where/when a gene is expressed; test enhancer/promoter activity"))
story.append(sp())

story.append(h2("RNAi (RNA Interference)"))
story.append(b("dsRNA introduced → Dicer cleaves → siRNA → RISC complex → targets complementary mRNA → degradation"))
story.append(b("Result: <b>gene knockdown</b> (reduced expression, not complete knockout)"))
story.append(sp())

story.append(h2("Traps"))
story.append(b("<b>Enhancer trap</b>: reporter inserted near endogenous enhancer → reports enhancer activity"))
story.append(b("<b>Promoter trap</b>: reporter only expressed if inserted downstream of active promoter"))
story.append(b("<b>Gene trap</b>: reporter contains splice acceptor → spliced into endogenous mRNA → disrupts gene"))
story.append(sp(6))

# ── SECTION 6: CRISPR ───────────────────────────────────────────────
story.append(h1("CRISPR-Cas9 GENOME EDITING (Lec 19)"))
story.append(sp())

story.append(h2("Mechanism"))
story.append(b("Guide RNA (gRNA) = crRNA (20 nt targeting sequence) + tracrRNA (scaffold)"))
story.append(b("crRNA matches target DNA; Cas9 cuts 3 bp upstream of <b>PAM sequence (NGG)</b>"))
story.append(b("DSB repaired by: <b>NHEJ</b> (error-prone → knockout) or <b>HDR</b> (precise edit with template → knockin)"))
story.append(sp())

story.append(h2("Designing crRNA"))
story.append(b("Find 20 nt sequence in gene followed by NGG (PAM) on the non-template strand"))
story.append(b("crRNA is complementary to the target strand (same sequence as non-template strand)"))
story.append(sp())

story.append(h2("Knockouts vs. Knockins"))
data5 = [
    ['Goal', 'Method'],
    ['Knockout', 'gRNA → NHEJ indels → frameshift → loss of function'],
    ['Conditional knockout', 'LoxP sites flank exon; Cre recombinase removes exon in specific tissue/time'],
    ['Knockin (CRISPR)', 'gRNA + HDR template containing desired sequence → precise edit'],
    ['Knockin (LoxP/Cre)', 'Insert LoxP-flanked selectable marker; Cre removes marker, leaves knockin'],
]
t5 = Table(data5, colWidths=[1.8*inch, 4.7*inch])
t5.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t5)
story.append(sp())
story.append(b("Antibiotic selection: cells with integrated transgene survive antibiotic; others die"))
story.append(b("Toxin selection (e.g., thymidine kinase + ganciclovir): kills random integrations, selects targeted"))
story.append(sp(6))

# ── SECTION 7: MODEL ORGANISMS ──────────────────────────────────────
story.append(h1("MODEL ORGANISMS (Lec 18)"))
story.append(sp())
story.append(b("<b>Why use them</b>: validate mechanistic genotype ↔ phenotype hypotheses"))
story.append(b("<b>Logistical requirements</b>: genetically tractable, culturable/breedable, short generation time, many progeny"))
story.append(b("<b>Biological requirements</b>: conserved functions with target organism (e.g., humans)"))
story.append(b("<b>Benefit</b>: concentrated community → shared tools, reagents, databases, protocols"))
story.append(sp())

data6 = [
    ['Organism', 'Strengths', 'Common Uses'],
    ['S. cerevisiae (yeast)', 'Fast, cheap, easy genetics, homologous recombination', 'Cell biology, gene function, protein interactions'],
    ['C. elegans (worm)', 'Transparent, invariant cell lineage, RNAi works well', 'Development, neuroscience, aging'],
    ['D. melanogaster (fly)', 'Fast generations, powerful genetics, balancer chromosomes', 'Development, behavior, genetics'],
    ['M. musculus (mouse)', 'Mammalian physiology, CRISPR/conditional KO', 'Disease models, immunology'],
    ['A. thaliana (plant)', 'Small genome, self-fertilizing', 'Plant biology, epigenetics'],
    ['Zebrafish', 'Transparent embryo, vertebrate, CRISPR-amenable', 'Development, drug screening'],
]
t6 = Table(data6, colWidths=[1.5*inch, 2.5*inch, 2.5*inch])
t6.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t6)
story.append(sp(6))

# ── SECTION 8: SELECTION ─────────────────────────────────────────────
story.append(h1("NATURAL SELECTION (Lec 21)"))
story.append(sp())

story.append(h2("Types of Selection"))
data7 = [
    ['Type', 'Effect on allele freq', 'Example'],
    ['Positive / Directional', 'Increases beneficial allele', 'Lactase persistence, antibiotic resistance'],
    ['Purifying / Stabilizing', 'Removes deleterious alleles', 'Conserved proteins (histones, tubulins)'],
    ['Balancing', 'Maintains multiple alleles', 'Sickle cell (het advantage), MHC diversity'],
    ['Neutral', 'No selection; drift governs freq', 'Synonymous mutations, non-functional regions'],
]
t7 = Table(data7, colWidths=[1.8*inch, 2.0*inch, 2.7*inch])
t7.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t7)
story.append(sp())
story.append(h2("Selected vs. Neutral Sites"))
story.append(b("<b>Selected sites</b>: functional sequence under selection (coding exons, regulatory regions)"))
story.append(b("<b>Neutral sites</b>: synonymous positions, pseudogenes, most intergenic DNA"))
story.append(b("dN/dS (ω): ratio of non-synonymous : synonymous substitution rates"))
story.append(p("&nbsp;&nbsp;&nbsp;&nbsp;ω > 1 = positive selection   |   ω ≈ 1 = neutral   |   ω < 1 = purifying selection"))
story.append(sp(6))

# ── SECTION 9: MICROBIAL SYMBIOSIS ───────────────────────────────────
story.append(h1("MICROBIAL SYMBIOSIS (Lec 22)"))
story.append(sp())
story.append(b("<b>Endosymbiosis theory</b>: mitochondria and chloroplasts derived from ancient bacterial endosymbionts"))
story.append(b("Evidence: double membrane, own circular DNA, 70S ribosomes, binary fission, similar gene sequences to bacteria"))
story.append(b("Bacteria: compact genomes, operons, no introns; Eukaryotes: large genomes, introns, more regulatory DNA"))
story.append(b("<b>Holobiont</b>: host organism + all its associated microbiota (microbiome); hologenome = combined genomes"))
story.append(b("<b>MWAS challenges vs. GWAS</b>: microbiome varies with environment/diet/time; OTU definition; causality harder; no fixed reference genome"))
story.append(sp(6))

# ── SECTION 10: PHYLOGENETICS ────────────────────────────────────────
story.append(h1("PHYLOGENETICS (Lec 23)"))
story.append(sp())

story.append(h2("Tree Terminology"))
data8 = [
    ['Term', 'Definition'],
    ['Root', 'Common ancestor of all taxa in tree'],
    ['Node', 'Branching point = common ancestor'],
    ['Branch', 'Lineage / evolutionary path between nodes'],
    ['Tip / Taxon', 'Terminal unit (species, individual, sequence)'],
    ['Clade', 'Group of taxa sharing a common ancestor (monophyletic group)'],
    ['Bootstrap value', 'Confidence in a node (0–100); >70 generally supported'],
]
t8 = Table(data8, colWidths=[1.3*inch, 5.2*inch])
t8.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t8)
story.append(sp())

story.append(h2("Inference Methods & Key Concepts"))
story.append(b("<b>Parsimony</b>: prefer tree requiring fewest evolutionary changes"))
story.append(b("<b>Distance</b>: cluster by pairwise sequence similarity (e.g., UPGMA, NJ)"))
story.append(b("<b>Maximum likelihood</b>: find tree maximizing probability of observing the data given a model"))
story.append(b("Only <b>shared, derived characters (synapomorphies)</b> are informative — they indicate shared ancestry"))
story.append(b("Characters: morphology, anatomy, behavior, DNA/protein sequences"))
story.append(b("<b>Gene tree ≠ species tree</b>: incomplete lineage sorting, horizontal transfer, or paralogy can differ"))
story.append(b("<b>Molecular clock</b>: neutral mutations accumulate at constant rate → date divergence events"))
story.append(b("Need many loci: substitutions saturate, recombination unlinks histories, selected loci bias results"))
story.append(b("COVID-19: viral mutations tracked transmission chains and outbreak origins phylogenetically"))
story.append(sp(6))

# ── SECTION 11: EXAM 1 CARRYOVER ────────────────────────────────────
story.append(h1("EXAM 1 CARRYOVER (likely still tested)"))
story.append(sp())

story.append(h2("Allele Types & Mutations"))
data9 = [
    ['Allele Type', 'Function', 'Dominance'],
    ['Amorphic (null)', 'No function', 'Recessive (usually)'],
    ['Hypomorphic', 'Reduced function', 'Recessive (usually)'],
    ['Hypermorphic', 'Enhanced function', 'Dominant'],
    ['Neomorphic', 'New function', 'Dominant'],
    ['Antimorphic (dom-neg)', 'Opposes WT', 'Dominant'],
]
t9 = Table(data9, colWidths=[1.6*inch, 2.2*inch, 2.7*inch])
t9.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t9)
story.append(sp())

story.append(h2("Mutation Types (coding sequence)"))
story.append(b("<b>Silent</b>: different codon, same amino acid (synonymous)"))
story.append(b("<b>Missense</b>: different codon → different amino acid"))
story.append(b("<b>Nonsense</b>: codon → stop codon (UAA, UAG, UGA) → truncated protein"))
story.append(b("<b>Frameshift</b>: indel not divisible by 3 → shifts reading frame downstream"))
story.append(b("<b>Loss of function</b>: nonsense, frameshift, deletion, inversion disrupting gene"))
story.append(b("<b>Pleiotropy</b>: one gene → multiple phenotypes"))
story.append(b("<b>Penetrance</b>: % of individuals with genotype who show phenotype"))
story.append(b("<b>Expressivity</b>: degree to which phenotype is expressed in those with genotype"))
story.append(sp())

story.append(h2("Gene Interactions (F2 ratios from dihybrid cross)"))
data10 = [
    ['Interaction', 'F2 Ratio', 'Clue'],
    ['Independent (no interaction)', '9:3:3:1', 'Four phenotypes'],
    ['Dominant epistasis (A over B)', '12:3:1', 'A dominant masks B'],
    ['Recessive epistasis (aa masks)', '9:3:4', 'aa masks B locus'],
    ['Duplicate recessive epistasis', '9:7', 'Need A AND B dominant for phenotype'],
    ['Reciprocal recessive epistasis', '9:6:1 or 9:3:4', 'Each recessive masks other'],
    ['Redundancy (duplicate dominant)', '15:1', 'Either A or B dominant enough'],
    ['Additivity', '1:2:1 or continuous', 'Additive effect of alleles'],
    ['Complementation (9:7)', '9:7', 'Both must have dominant allele'],
]
t10 = Table(data10, colWidths=[2.3*inch, 1.3*inch, 2.9*inch])
t10.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#1a1a5e')),
    ('TEXTCOLOR', (0,0), (-1,0), colors.white),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 7),
    ('FONTNAME', (0,1), (-1,-1), 'Helvetica'),
    ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.white, colors.HexColor('#f0f0f8')]),
    ('GRID', (0,0), (-1,-1), 0.3, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ('LEFTPADDING', (0,0), (-1,-1), 3),
    ('RIGHTPADDING', (0,0), (-1,-1), 3),
    ('TOPPADDING', (0,0), (-1,-1), 2),
    ('BOTTOMPADDING', (0,0), (-1,-1), 2),
]))
story.append(t10)
story.append(sp())

story.append(h2("X-linked Linkage & Recombination"))
story.append(b("Notation for linked alleles: <b>AB;ab</b> (not AaBb)"))
story.append(b("Males (XY) are hemizygous for X-linked genes → show X-linked phenotypes with one allele"))
story.append(formula("Parental class freq = (1 − RF) / 2 each   |   Recombinant class freq = RF / 2 each"))
story.append(b("RF = recombination frequency (map distance in Morgans/cM)"))
story.append(b("Penetrance problem: P(affected) = P(genotype) × penetrance"))
story.append(sp(4))

story.append(hr())
story.append(Paragraph("Good luck! — BME 105 Winter 2026 Exam 2", ParagraphStyle('footer',
    parent=styles['Normal'], fontSize=8, alignment=TA_CENTER,
    textColor=colors.HexColor('#555555'), spaceBefore=4)))

doc.build(story)
print("PDF created successfully.")
