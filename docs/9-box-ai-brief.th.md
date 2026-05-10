# DoiBean — 9-Box AI Solution Brief

> สำหรับกรอกใน Custocare 9-Box AI Solution Brief Workshop Tool
> https://aisolutionbreif.netlify.app/
>
> **โครงการ:** DoiBean — AI co-pilot สำหรับชาวสวนกาแฟ specialty
> **Sector:** AgriTech / Verified-Origin Platform
> **วันที่:** พฤษภาคม 2026

---

## 1. PROBLEM — ปัญหา

ชาวสวนกาแฟ specialty ดอยช้าง ขายเมล็ดเขียวได้กิโลละ **฿100** แต่ร้านคาเฟ่ขาย **฿2,500** ต่อกิโล — ส่วนต่าง **25 เท่า** ชาวสวนได้แค่ **4%** ของมูลค่าสุดท้าย

เกิดจาก 3 ปัญหาที่แก้ได้:

- **ข้อมูลไม่สมมาตร** — ชาวสวนไม่รู้คะแนน SCA ของเมล็ดตัวเอง ไม่รู้ defect ไม่รู้ flavor profile
- **ไม่มีช่องทางขายตรง** — ชาวสวนเก่งแค่ไหน ก็ไม่สามารถส่งให้ roaster โตเกียว/เบอร์ลินตรง (ขั้นตอน export, ภาษา, trust)
- **ปลูกผิดสายพันธุ์ในอีก 5 ปี** — climate ขยับเขตปลูกขึ้นที่สูง ~150 ม./ทศวรรษ สายพันธุ์ที่ปลูกวันนี้ผลผลิตจะลด 25% ในปี 2035

**ความถี่:** ทุกฤดูเก็บเกี่ยว (รายปี) + ทุกการตัดสินใจปลูกใหม่ (ทุก 5–7 ปี)

---

## 2. WHO SUFFERS — ใครเดือดร้อน

- **3,921 ครัวเรือนชาวสวน specialty** ในเชียงราย (ตัวเลขปี 2025, +25% จากปี 2020) — กลุ่มหลัก
- **ชาวเขา (อาข่า ลีซู)** ที่ระดับ 1,200–1,420 ม.
- **Roaster โตเกียว / เบอร์ลิน / โซล** ต้องการ traceability + คุณภาพคงที่ แต่ติดอยู่กับการซื้อผ่านผู้ส่งออกที่ไม่โปร่งใส
- **ภาครัฐไทย** — เสีย GDP export ให้ middlemen markup ที่ไหลออกประเทศ
- **ผู้บริโภค** จ่ายราคา premium โดยไม่รู้ origin จริง

---

## 3. CURRENT WORKAROUND — วิธีแก้ปัจจุบัน

- ขายผ่าน **สหกรณ์ในราคา commodity** (price-taker, ไม่มีคะแนนคุณภาพ)
- คุณภาพประเมินจาก **Q-grader ของผู้ส่งออก** — ชาวสวนไม่เห็นคะแนน
- คำแนะนำสายพันธุ์จาก **เจ้าหน้าที่ส่งเสริมการเกษตร** ข้อมูลล้าสมัย ไม่มี climate model
- **Excel + สมุดจดมือ** สำหรับติดตามผลผลิต
- หา roaster จาก **trade show + อีเมล** — ช้า, trust ต่ำ
- ชำระเงินผ่าน **Western Union / SWIFT manual** — ค่าธรรมเนียมสูง ไม่มี escrow

---

## 4. AI TASK — งาน AI

| Task | รายละเอียด |
|------|------------|
| ☑ **Classify** | ตรวจจับ defect บนเมล็ดเขียว (SCA Cat-1 / Cat-2 taxonomy 30+ class) |
| ☑ **Predict** | ทำนายผลผลิตสายพันธุ์ภายใต้ IPCC scenarios ปี 2030/2040 ตาม GPS แปลง |
| ☑ **Recommend** | แนะนำสายพันธุ์ทนสภาพอากาศตามระดับความสูง + ดิน + microclimate |
| ☑ **Detect** | โรคใบสนิม (roya), ด้วงเจาะผลกาแฟ, anthracnose จากภาพถ่ายของชาวสวน |
| ☑ **Extract** | ทำนาย cupping notes จาก visual analysis ของเมล็ดเขียว |
| ☑ **Generate** | แปล Thai → ภาษา roaster (English / Japanese / Korean) เล่าเรื่อง origin |

---

## 5. DATA NEEDED — ข้อมูลที่ต้องการ

### มีอยู่แล้ว

- ชุดข้อมูล SCA สาธารณะ 5,000 ภาพ พร้อม defect labels
- IPCC RCP4.5 / RCP6.0 projections (2030, 2040)
- ข้อมูล GIS ชั้นดินจากกรมพัฒนาที่ดิน (DOA)
- ข้อมูล climate ย้อนหลัง 20 ปีจาก TMD
- Mapbox / OSM สำหรับ plot mapping

### ต้องเก็บเพิ่ม

- **ภาพเมล็ดเขียวไทย 2,000+ ภาพ** balance ตาม defect class (ปัจจุบัน 500 ภาพ = underfit ~16/class)
- GPS pin + altitude + slope/aspect ของแปลงนำร่อง
- ผลเก็บเกี่ยวต่อแปลงต่อฤดู (สำหรับ data flywheel — ต้อง 2 ฤดูขึ้นไป)
- คะแนน Q-grader คู่กับคะแนนโมเดล (validation set)
- รายงานโรค/แมลงต่อพื้นที่ลุ่มน้ำ (hyperlocal outbreak map)

### แหล่งข้อมูล

ความร่วมมือดอยตุง (3 ฟาร์มนำร่อง), สหกรณ์กาแฟดอยช้าง, API จาก TMD/DOA (ฟรี), citizen science จากผู้ใช้แอป

---

## 6. HUMAN LOOP — มนุษย์ในวงจร

- **Q-grader override** เมื่อ confidence < 90% หรือคะแนนต่างจาก manual >2 SCA จุด → ส่ง review
- **Farmer veto** ในการเลือกสายพันธุ์ — โมเดลแสดง top 3 พร้อม SHAP explanations ชาวสวนเลือกเอง
- **Admin approval** สำหรับ onboarding roaster (KYC, payment terms, trade history)
- **Lot signoff** โดยผู้ส่งออกก่อนส่งระหว่างประเทศ (compliance + ประกัน)
- **คณะกรรมการระงับข้อพิพาท** เมื่อคะแนนไม่ตรงกัน: Q-grader 2 คน + ตัวแทนชาวสวน 1 + ตัวแทนแพลตฟอร์ม 1
- **Climate disclaimer** — ผลลัพธ์ variety advisor ต้องแสดง uncertainty band และให้ชาวสวน acknowledge ก่อนตัดสินใจปลูก

---

## 7. OUTPUT / RESULT — ผลลัพธ์

| Format | รายละเอียด |
|--------|------------|
| ☑ **Dashboard** | แอปมือถือชาวสวน — ประวัติสแกน, lot ปัจจุบัน, ราคา offer, สถานะการชำระ |
| ☑ **Alert** | ช่วงเก็บเกี่ยวเปิด, โรคระบาดในลุ่มน้ำ, ได้รับ offer จาก roaster |
| ☑ **Report** | Lot Quality Sheet (PDF, ไทย+อังกฤษ) — คะแนน SCA, defect, cupping notes, ภาพ, GPS — ให้ roaster |
| ☑ **Action** | ชำระตรงผ่าน PromptPay / Stripe Connect เมื่อ roaster ยืนยัน + auto-generate เอกสาร export |

---

## 8. SUCCESS METRIC — ตัวชี้วัดความสำเร็จ

### ตัวชี้วัด tech

- ความแม่น Cat-1 defect ≥**85%** บนเมล็ดไทย
- ความสัมพันธ์คะแนน SCA ±2 จุดเทียบ Q-grader manual (validation set)
- TFLite inference < 2 วินาที บน Snapdragon 4xx (Android ราคาถูก)

### ผลลัพธ์ชาวสวน (นำร่อง 100 ฟาร์ม 24 เดือน)

- รายได้ต่อกิโลเมล็ดเขียว ≥ **฿1,400** (เทียบ ฿100 baseline = ดีขึ้น 14 เท่า)
- รายได้สุทธิชาวสวน **+3 เท่า** ใน 24 เดือน

### Marketplace

- ปิด 1 transaction ดอยช้าง → โตเกียว/เบอร์ลิน ใน 60 วันแรก
- 50 ชาวสวน + 5 anchor roasters ภายในเดือนที่ 12
- 200 ชาวสวน + 20 roasters ภายในเดือนที่ 24

### ระดับจังหวัด (NDEA Chiang Mai Digital Economy)

- มูลค่า verified-origin export จากเชียงใหม่ **+฿50M** ต่อปี ภายในปีที่ 2
- ขยาย sector — กาแฟ → ชา → สมุนไพร → น้ำผึ้ง บนแพลตฟอร์มเดียวกัน

---

## 9. RISK — ความเสี่ยง

| ความเสี่ยง | การ mitigate |
|------------|--------------|
| **Data privacy / PDPA** — GPS, รายได้, ข้อมูลพืชของชาวสวนเป็นข้อมูลอ่อนไหว | เก็บใน device เท่าที่ทำได้, ใช้ THaLLE local LLM (ไม่ส่งออก Anthropic API), ขอ consent ชัด + ยกเลิกได้ |
| **Variety advisor liability** — แนะนำผิด = ชาวสวนเสีย 4–7 ปี | SHAP explanations + uncertainty band + farmer override + disclaimer + ประกันภัย |
| **Tech sovereignty** — stack ปัจจุบันใช้ Anthropic Claude (US) + AWS = ความเป็นเมืองขึ้น | เปลี่ยน LLM เป็น THaLLE (KBTG open-source), ใช้ NIPA/CAT cloud, train บน LANTA supercomputer |
| **Algorithmic bias** — โมเดล defect train จากเมล็ด Latin America อาจ misclassify สายพันธุ์ไทย | ชุดข้อมูลไทย 2,000+ ภาพก่อน launch + audit ต่อเนื่องกับ Q-grader ชาวเขา |
| **Two-sided cold-start** — roaster โตเกียวไม่เชื่อคะแนน CV จากแอปไทยที่ไม่รู้จัก | anchor 1 trusted Thai/Japanese specialty buyer ก่อน + Q-grader manual co-sign 50 lot แรก |
| **สหกรณ์ตอบโต้การเมือง** — อาจ lobby ออกกฎ "certified-export" บล็อกแพลตฟอร์ม | ผ่าน NDEA + สำนักงานอุตสาหกรรม + extension services — วางตำแหน่งเป็น "ส่งเสริม" ไม่ใช่ "แทนที่" |
| **Solo founder concentration** — มอนด์ทำ 4 บทบาท: product + farmer relations + engineering + roaster sales | หา co-founder (เชียงราย) + CTO + designer ภายใน 60 วัน — ถ้าไม่ได้ อย่าเพิ่งระดม pre-seed |
| **Climate model ผิด** — IPCC RCP6.0 อาจเป็นความจริงจริงๆ ไม่ใช่ RCP4.5 | re-run คำแนะนำรายปี + soft-launch ในฐานะ "guidance" ไม่ใช่ "prescription" |

---

## Template Suggestion

สร้าง template ใหม่ใน Custocare workshop tool ชื่อ:

> **"DoiBean — AgriTech Verified-Origin"**

ใช้ซ้ำได้กับ AgriTech farmer-app brief อื่นๆ (ชา, สมุนไพร, ข้าวพันธุ์พิเศษ, น้ำผึ้ง)

---

*สรุปจากการประชุมบอร์ดที่ปรึกษา 8 ท่าน 3 รอบ — Almondo-local Boardroom · พฤษภาคม 2026*
