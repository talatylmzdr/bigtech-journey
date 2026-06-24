# Big Tech Journey — KONTROL MERKEZİ (Revize)

> **Bu dosya ne?** Günlük yol haritasının (`Talat-BigTech-Journey-12-Hafta.md`) **üstünde duran kontrol katmanı.**
> Günlük detay, örnekler, YouTube kanalları, kod parçaları **o dosyada kalıyor** (silinmedi). Bu dosya iki şeyi ekler:
> 1. **Birleşik Durum Panosu** — her konuda + her gerçek projede *bugün nerede olduğumuz* (tek bakışta).
> 2. **Gerçek Proje Entegrasyonu** — plandaki "oyuncak" projeleri **senin gerçek projelerinle** değiştirir.
>
> HOMER.OS'taki `CLAUDE.md` (kısa context) + `agent_docs/` (detay) ayrımının aynısı: bu = CLAUDE.md, 12-Hafta dosyası = detay.
> **Tarih:** 24 Haziran 2026 · her gün/hafta bu panoyu güncelle.

---

## 🎯 Temel fikir: öğrendiğin yığın = zaten çalıştığın yığın

Planın güçlü ama jenerik projeler kullanıyordu. Senin **haksız avantajın**: o jenerik projeler birebir senin gerçek projelerinin aynısı. Onları değiştiriyoruz:

| Plandaki jenerik proje | Senin gerçek karşılığın | Durum |
|---|---|---|
| Faz 2 — "Personal Knowledge API" (FastAPI+Postgres+Docker+Auth) | **SAP LicenseHub** (aynı yığın!) | POC iskeleti **kuruldu** |
| Faz 3 — "Embeddings & RAG" | **HOMEROS** (Voyage+pgvector **canlı**) | Skor Faz 0-5 canlı |
| Faz 3 — "Tool Use & Agent" / Showcase | **KAMİRAN** (AI itibar platformu) | Teknik tasarım **bitti** |

Yani FizzBuzz hissi geçecek: temelleri bitirir bitirmez **gerçek, canlı production kodu** üstünde öğreneceksin. "Sağlam yol > hızlı yol."

---

# BÖLÜM A — BİRLEŞİK DURUM PANOSU

> Her konuda + her projede nerede olduğumuz. **Bunu güncel tut** — sabah açınca "bugün neredeyim" bir bakışta görünsün.

## A1 — Öğrenme konuları (nerede kaldık)

| Konu | Durum | Şu an nerede | Sıradaki |
|---|---|---|---|
| **Python temeli** | 🟡 Devam (H1) | Gün 1-3 bitti: kurulum, değişken/string, if/else + döngü (FizzBuzz, guess) | Gün 4: liste/dict/set → Gün 5: fonksiyonlar |
| **Modern Python** (type/test/uv/ruff) | ⚪ Başlamadı | — | Hafta 3 |
| **Backend** (FastAPI/Postgres/Docker/auth) | ⚪ Başlamadı | — | Hafta 4 (→ SAP ile) |
| **AI Eng** (LLM/RAG/agent/eval) | ⚪ Başlamadı | — | Hafta 8 (→ HOMEROS/Kamiran ile) |
| **DSA / LeetCode** | ⚪ Başlamadı | — | Hafta sonu 2-3 Easy (Two Sum, Contains Duplicate, Valid Anagram) |
| **İngilizce** | 🟡 Devam | Tema 1: kendini tanıtma | 60sn tanıtım kaydı |
| **GitHub streak** | 🟢 Aktif | Day 3 push'landı | Her gün ≥1 commit (hedef 84 yeşil kare) |

Durum kodları: 🟢 canlı/akıyor · 🟡 devam ediyor · ⚪ başlamadı · 🔴 bloke

## A2 — Gerçek projeler (nerede kaldık)

| Proje | Durum | Nerede kaldık | Sıradaki adım | Engel |
|---|---|---|---|---|
| **HOMEROS** (homer-os) | 🟢 Canlı | AI Skoru Faz 0-5 canlı + main'e merge; 751 skor; re-embed sonrası "Mükemmel" 39; etkileşim alt-ağırlıkları aktif | Migration 68'i Supabase'de apply; arkadaşın UI build'i; bot NULL scrape | Voyage ücretsiz tier (3 RPM) — cron'da throttle/ödeme gerek |
| **KAMİRAN** | 🟡 Tasarım bitti, kod yok | Fizibilite + operasyon + teknik tasarım hazır (`kms.os\KAMİRAN\`); multi-tenancy + ayrı repo kararı | Seç: (1) SQL migration, (2) Faz 0 test, (3) Modül 1 ekran | Faz 0 belirsizlikleri (Primetag X, motor API maliyeti) |
| **SAP LicenseHub** | 🟡 POC iskeleti kuruldu | FastAPI+SQLAlchemy+SQLite, mock connector, smoke test 10/10; OData keşif kiti hazır (`PBS lisans\licensehub\`) | Diğer bilgisayarda `discover_sap.py` çalıştır → çıktıyı getir → connector'ı kilitle | SAP başka bilgisayarda |

> Detaylı "nerede kaldık" her projenin kendi dosyasında:
> HOMEROS → `homer-os/CLAUDE.md` + `agent_docs/homeros_score.md` ·
> KAMİRAN → `kms.os/KAMİRAN/KAMIRAN_Teknik_Tasarim.md` ·
> SAP → `PBS lisans/licensehub/README.md`

## A3 — Konu ↔ Proje eşlemesi (hangi öğrenme hangi projeyi besliyor)

| Öğrenme konusu | Hangi gerçek projede uygulanıyor |
|---|---|
| Python temeli, type hints, test | Üçü de (SAP POC zaten Python+type+pytest) |
| FastAPI, Pydantic, REST | **SAP LicenseHub** (zaten FastAPI) |
| PostgreSQL, SQLAlchemy, Alembic, Docker | **SAP LicenseHub** (SQLite→Postgres, Alembic ekle, Dockerize) |
| Auth, JWT, multi-tenant, deploy | **SAP** (tenant izolasyonu) + **Kamiran** (agency_id) |
| LLM API, structured output, prompt cache | **HOMEROS** (`lib/ai/label-influencer.ts`) + **Kamiran** (sentiment/AEO) |
| Embeddings, pgvector, RAG, semantic search | **HOMEROS** (`lib/embed.ts`, Voyage 1024d — canlı) |
| Agent, tool use | **Kamiran** (AEO ölçüm + sosyal dinleme aksiyonu) |
| Eval & observability (en kıymetli) | **HOMEROS** (match kalitesi, skor kalibrasyon) + **Kamiran** (maliyet kontrol) |

---

# BÖLÜM B — GERÇEK PROJE ENTEGRASYONU (revize proje track'i)

> 12-Hafta dosyasındaki günlük konular **aynen geçerli** (oradan çalış). Burada o haftaların **projesini** gerçek projenle değiştiriyoruz. Yani: konuyu 12-Hafta dosyasından öğren, **uygulamayı bu gerçek projede yap.**

## Faz 1 (Hafta 1-3) — Python temeli · *genel kalır*

Temel alıştırmalar (FizzBuzz, todo_cli, math_utils...) **kalsın** — kas hafızası lazım. Ama "neden" şu: bu temelleri biter bitmez **SAP LicenseHub kodunu okuyabileceksin** (zaten Python+FastAPI+SQLAlchemy). Hafta 3 bitince `PBS lisans\licensehub\app\` içini aç, ne anladığını test et — ilk gerçek kod okuman.

**Bağlantı görevi (Hafta 3 sonu):** SAP POC'taki `app/models.py`'yi aç, SQLAlchemy modellerini Hafta 2 OOP/dataclass bilginle eşleştir.

## Faz 2 (Hafta 4-7) — Backend · **PROJE = SAP LicenseHub** (knowledge-api yerine)

Plandaki "Personal Knowledge API" yerine **gerçek SAP LicenseHub'ı** büyüt. POC iskeletini zaten kurduk; her hafta bir katman ekliyorsun:

| Hafta | 12-Hafta konusu | SAP LicenseHub'da uygulama |
|---|---|---|
| **4** | HTTP, REST, FastAPI, Pydantic, DI | POC zaten FastAPI. Endpoint'leri incele/genişlet (`/systems/{id}/measure`); Pydantic şemaları (`app/schemas.py`) derinleştir |
| **5** | PostgreSQL, SQLAlchemy, Alembic, Docker | **SQLite → Postgres** geçir (config'de hazır); Alembic migration ekle (şu an `create_all`); `docker-compose` ile Postgres |
| **6** | Auth, JWT, deploy, observability | Multi-tenant auth (firma bazlı); structured logging; Railway/deploy; `/health` |
| **7** | PROJE 1 cilası | Gerçek OData connector'ı doldur (`odata.py`) — keşif çıktısı gelince; README + demo |

**Sonuç:** Faz 2 bitince elinde *jenerik bir todo API* değil, **gerçek bir SAP ürünü** olur — mülakatta "SAP danışmanıyken kendi lisans otomasyon backend'imi yazdım" hikayesi (1000 jenerik aday arasında ayırt edici).

## Faz 3 (Hafta 8-12) — AI · **PROJE = HOMEROS + KAMİRAN**

| Hafta | 12-Hafta konusu | Gerçek projede uygulama |
|---|---|---|
| **8** | LLM API (Anthropic/Gemini), structured output, streaming | **HOMEROS** `lib/ai/label-influencer.ts`'i oku — lazy client, prompt cache, tool_use+Zod, token sayımı. Çalışan production LLM kodu. |
| **9** | Embeddings & RAG, pgvector | **HOMEROS** `lib/embed.ts` (Voyage 1024d) + `match_for_brief_v3` (pgvector cosine). RAG'ın canlı hali. Semantic vs full-text karşılaştır. |
| **10** | Tool use & agent | **KAMİRAN** Modül 2: AEO ölçüm hattı + sosyal dinleme aksiyon motoru (tool-using). Tasarım `KAMIRAN_Teknik_Tasarim.md` Bölüm 3'te. |
| **11** | Eval & observability (en kıymetli) | **HOMEROS** skor kalibrasyonu (percentile, `agent_docs/homeros_score.md`) + **Kamiran** maliyet kontrol katmanı. "Sayısal iyileştirme" hikayesi. |
| **12** | SHOWCASE + iş arama | Aday 1: **Kamiran Modül 1** (kitle analizi, devşirilebilir) canlıya. Aday 2: plandaki "Audit Log Intelligence" (SAP'a oturur). Birini seç, demo + blog. |

**Sonuç:** Showcase'in jenerik değil — ya canlı bir influencer AI platformu (Kamiran) ya da SAP-security + AI hibriti. İkisi de senin biricik hikayene oturuyor.

---

# BÖLÜM C — Günlük rutin & panoyu güncelleme

Günlük/haftalık rutin **12-Hafta dosyasındaki gibi** (saat şablonu, pomodoro, journal, commit, retro). Buraya ek tek kural:

**Pano güncelleme kuralı:** Her hafta sonu retrosunda (Pazar) **Bölüm A panosunu** güncelle:
- A1: hangi konu 🟡→🟢 oldu, şu an neredesin.
- A2: gerçek projelerde bir şey ilerledi mi (HOMEROS commit, Kamiran kararı, SAP keşif).

Böylece her an "her konuda nerede olduğumuzu" tek dosyada görürsün — istediğin buydu.

**Günlük 3 cümle** (journal.md) aynen: ne yaptım / neyi anlamadım / yarın ne.

---

# BÖLÜM D — Hızlı linkler

> 📍 Bu dosya **bu repo'nun kökünde** (`bigtech-journey/KONTROL-MERKEZI.md`). Planlama dökümanları repo dışında `Desktop\work\influencer\` klasöründe.

| Ne | Yer |
|---|---|
| **Bu kontrol merkezi** | repo kökü: `KONTROL-MERKEZI.md` |
| Günlük commit / journal / habit-tracker / retro | `tracker/` (bu repo) |
| Günlük kod projeleri | `projects/` (bu repo) |
| **Günlük detay yol haritası** (örnek, YouTube, kod) | `Desktop\work\influencer\Talat-BigTech-Journey-12-Hafta.md` |
| 12 aylık üst strateji | `Desktop\work\influencer\Talat-BIGTECH-12-Aylik-Yol-Haritasi.docx` |
| **SAP LicenseHub** (Faz 2 projesi) | `Desktop\PBS lisans\licensehub\` |
| **KAMİRAN** (Faz 3 projesi) | `Desktop\kms.os\KAMİRAN\` |
| **HOMEROS** (Faz 3 projesi, canlı) | `Desktop\homer-os\` |

---

## Özet — bu revizyon ne değiştirdi?

1. **Eklendi:** Birleşik Durum Panosu (Bölüm A) — her konuda + her projede nerede olduğumuz, tek bakışta. (Senin asıl isteğin.)
2. **Değişti:** Jenerik projeler → gerçek projeler (SAP=Faz 2, HOMEROS+Kamiran=Faz 3).
3. **Korundu:** 2595 satırlık günlük plan, örnekler, YouTube kanalları, İngilizce, DSA, takip sistemi — hepsi 12-Hafta dosyasında duruyor.

> "Bu günleri bitirince iyi bir yol haritamız olsun" dedin — artık günlük plan + gerçek proje + canlı durum panosu birbirine bağlı. Her sabah bu dosyayı aç, panoya bak, o günün işine 12-Hafta dosyasından devam et.
