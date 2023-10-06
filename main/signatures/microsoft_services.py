# storing the service names hashed for improved name up look times
microsoft_services = [
    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7a026f6e9ec718812d962441896afe89248f0cf39e1a352851f696cfbf96405d", # [ALG] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4cf97ad16ea053bb107275e94f0509fe5e00b5771d71dc7032c7e13e531508d4", # [Appinfo] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2ea69fa906e55aaa555c0e0fcde9a1dc8cd2e303260dd88a0dedf779d9f7b2f3", # [AppMgmt] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6de91d990efe8d2c091b89e9b5aac0e76648400e3123a842877fd29f57fa5302", # [Audiosrv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a4aeb969472a21acd7c8a9543ae9d02eee79ef7aed91b89b07f866e0ec9a6a12", # [AppXSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "13485ca7c960618e1fef1bf36435b7a2e76dac4b69a76a11d9ec481499e535fc", # [autotimesvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d58854a40fb6ff4310c498ad74000afd718098571327aa3d448b813f8597184b", # [AppVClient] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 58FD671E2D4D200CE92D6E799EC70DF96E6D2664
    "5b22ba8e5db4143abeba6473826c96542fa305ad2c32096ed250a95d7f6b2f7d", # [AudioEndpointBuilder] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "09f3dd4dc97b4d45e3841d2b272c5228a4ab7a299a569ba3745581fab2c0932c", # [AssignedAccessManagerSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8de6b16e2b574d1a934cfc53e45c3ff7244d6f134bd6dc35b88bb9820d27d4e0", # [AJRouter] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "12de0e5d4709aa095b198dddeaf69139b5b9a44f19d33f653987402dd7767dfd", # [AppIDSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0eabf5ec37da1813d3e8838e6aa6ce90e053ef72c9cb533b8eda594a64d5b386", # [AppReadiness] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b14d37333ad253f04c60effd345bf99d4921599fe77bb4eb443a105fe8bf3859", # [BrokerInfrastructure] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fbeb4c4fac309752175c195519188744733be86a39908fc7beeef517812cebfa", # [BthAvctpSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e33c1929adf587777720424ab1b15ab8598ff835c8f1c1ab64a2cf69bb108978", # [AxInstSV] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "db9af313ee43a44ddc314fa0d16c63dd121b3786d2ef6b4225418392c783a4f9", # [BDESVC] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "69af6f387b18fc59de120037c5f294175e3b2172ed9fdd6f12b7800b77cc710b", # [bthserv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "88f3305a5dd067e3ff15ba0d2416a8fd431ac03848e4d45ab6b60f2484023230", # [camsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9799b10a51f0325d335fda867ad0fa4001756502aff45f4b9b5329b79a633d71", # [BTAGService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "94383f71bb67e1abe7b5f06eab59a146924dea7bf9362394ef5fc528051d48d1", # [BITS] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "428d4b8e0e3f0cf209078a27f8e1c649d577ac7482558919373d1ca51eaa03a6", # [BFE] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "70654f5955b415b6d64fbf516e363bcf2d92b73ebc56519f1bf8a998ad6c8e4d", # [CDPSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c41752674c3ede51fdcfab629c2c9b1de3572b6848fa8e5534c915086ce794a1", # [CertPropSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e5ba126bf0b92c6e6d600b7326785d89690eef77e18404f2550ceb22cb138c88", # [ClickToRunSvc] - Valid Windows Service. Issuer : CN=Microsoft Code Signing PCA 2010, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 7C94971221A799907BB45665663BBFD587BAC9F8
    "d12824ade176fe5405aa4b79c45fdbc37b72e75f9331227d170f40bcebcb39f5", # [cloudidsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "bc6e52a4e274510b8e70abb39572e3aa61d225c312f780dba2f07cf14f1e5702", # [CscService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0cf733b31bf5cbb775254ed8f4674af90e525dc5242dea87f9c737724aed5784", # [COMSysApp] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b0f946064eedf37387736d2fd23fdc22fcb8e7967753c80c9f92671f9aa727aa", # [ClipSVC] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "dbd7f8ceb458e6b2391f4740e54a0c0cb769cd14574968a012e10a43c5a61b5d", # [dcsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f8f5e567fdd60b20515f59a17b00868cb028610963661167c87895e564564b3b", # [CoreMessagingRegistrar] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "70f8dd692406fdfa44b7c86524588d967a0085c2e2ef95a6fdfc0cc1057ebfa9", # [defragsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3d388a53ac9d825a49488be04e1a226169d0b7db340cd35fff59efbc018ff4fd", # [CryptSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6ed28873e50feaa611070e4b721714186c171b0a3f659de24d2148bb224c8799", # [DcomLaunch] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4f7564cac274d1739bcf8992c139b1ede8c7bd0320663ba50a8f69e4c4f504b7", # [DeviceAssociationService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fceb40852b2c368b54a8958f17efdf9e81a80b12b4ec93f67444e14e199c4a83", # [DeviceInstall] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "ada3925d83c0f8ab8361ebc855e22675e8dfffb6bb26095c9aa8fafafbddace8", # [DevQueryBroker] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f8771fa955d6b96bab344a10951353351dd527b4a47dd87f7de757f7c522d642", # [Dhcp] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2fc0f539697e0a48107ee72b505487b9d889cdaf3a4a39ede21e437058ef627d", # [diagsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b936a49ef90c06286956980a4980ed709962b9e0d18e0163512261d96f39cd88", # [diagnosticshub.standardcollector.service] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "370b97a99d67fb0e70e61561ba0e650896769e89f976c460c40ba48b62c1070f", # [DispBrokerDesktopSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5b2886863fcb7d1833c8f25256b67a7fc19eaf5bb8d64599f104112f800f7dec", # [DiagTrack] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9106d284de3ec6a8e70fe2ecf8ee87ba02d01dd236367339d53377c06679c7b3", # [dmwappushservice] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "22d431c245cbbea00fcdea8ef274258d7b913b72c45d2a6366db18ea5d225caa", # [DialogBlockingService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c5f6171438d71f3a63b574314817849c0c649a32d4a60eccb6848080a1638edd", # [DmEnrollmentSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d176ad527c2ba0b7a6605d201cd5ca2737fec4ed895dfdcd489589ba76e09743", # [DisplayEnhancementService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e41365a3027ea60bd3b7c5fe813d3ad9357b78ae1d26db70762742f0060a74e4", # [Dnscache] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e571b32f3eeb3081b5d1567b28136d338be0ce8df724dc2b102665e3be90630e", # [DoSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "16f88e7c966c420905390365ca5667215bee79595c40031d9a933947e8d05b1f", # [dot3svc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "caece7f58fce2c0d73a12af487b289e60a5ea4d682f6b0b160a3969fb7d9dad0", # [DPS] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "61b6fbc1c66a4f882ed362fde0506084f5fd628fff782d3017fc658b20ed2f4e", # [DsmSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5e3aa1a355f2e0c50185932ed441d73d09dc1c7256ca8e45766e571b1b505bcb", # [DsSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "55d6310c1a7c455a8582502be8926dfaf8fb98b8aff34e6aba12759e35512262", # [edgeupdatem] - Valid Windows Service. Issuer : CN=Microsoft Code Signing PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 7CB6F13D24E9A7244B65CF7A48E8ED6170CD6C77
    "82cddab067a9f263922e50396fe13e584f82b34fcba9ee44b4d0c29501604d15", # [DusmSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "af83d6ad358fb429b7e28cc4e87881d9f63178f39e8f85626383fc455e23fc13", # [edgeupdate] - Valid Windows Service. Issuer : CN=Microsoft Code Signing PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 7CB6F13D24E9A7244B65CF7A48E8ED6170CD6C77
    "17c72a08444159f04a59188d53af30f0dcfc2ef56d1e25bf2fc78845935f51f2", # [Eaphost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "ea9ac95b21cd4848eb59fe905000425ee35d2903dfe4e5118efcdb65da7df1fe", # [EFS] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5303cbf5953d4dc2a21a614201e44676cb5e3398c08d8c5a35070df0894663c1", # [embeddedmode] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "68a5a7ab08518ba038a45b4194c4e81bcb5adc4982bb1159fe960fe85cb91095", # [EntAppSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e6e9fa4320e8cc1688901fa1597f356136ef81a772d33de9667c1e028f62f116", # [EventLog] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "cb4169c53665e7e9d18871b5b8d541752fba55dde75fc93eb3cf6cd113972db8", # [EventSystem] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "77b6dcbf812e159fe806b8469d7407302a7051b6ee266acf4a67ecfc475a7926", # [FDResPub] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "00d84ab46e6345e15e7303f9a125b1d23cc5f5e804cc79e0fa1ada9801507bba", # [Fax] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8d0093eec0bab72eaf19635dde33d76df668a33a11a0034fc5519953cd438b3c", # [fhsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "050a946b52ba18f9d592458b19d28de94114e07d2efe88081aa69f549de1f354", # [fdPHost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a39f4a16c1742633cf969ca483be9efd89b81cf68456c4002fe66e1b3ed89aee", # [FontCache] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "538160d0c04d5e994f4ceaa1e48bc55fe047f5dd3179df04b285c0774bb0ea35", # [FrameServer] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b65a99e03d4649b134ea8d820c9fb8c20033371936c87838dd4aa8ff67e11383", # [GoogleChromeElevationService] - Valid Windows Service. Issuer : CN=DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1, O="DigiCert, Inc.", C=US

    # Thumbprint : 2673EA6CC23BEFFDA49AC715B121544098A1284C
    "f0580d902cf7ffaaa7946d7d68ae4abc42b79ee7b1b307b60fb6e7ac7ea1042e", # [gpsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "07b9dc765ce0ecfe9a61ded4059020427abd41978d902b01038ce977939618c3", # [GraphicsPerfSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "259bfbe7afd37ee2dbd4faa43fc3fdc111b02abeff3ceb2bff464ef09fe0e5d9", # [gupdate] - Valid Windows Service. Issuer : CN=DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1, O="DigiCert, Inc.", C=US

    # Thumbprint : 2673EA6CC23BEFFDA49AC715B121544098A1284C
    "ef9d75611a3031e9e5acd35cf5386230ce653ed620e92b6a1a02934f29a15570", # [gupdatem] - Valid Windows Service. Issuer : CN=DigiCert Trusted G4 Code Signing RSA4096 SHA384 2021 CA1, O="DigiCert, Inc.", C=US

    # Thumbprint : 2673EA6CC23BEFFDA49AC715B121544098A1284C
    "b1ccc71b1e689376ab59f36c57cf8837692357467d3e19546541344bed1b76e1", # [hidserv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e243e085644157c1d20dcd82e76c25ce3095ae928617c1c4b1b1abb339a7bb3a", # [HvHost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2f06d10415ffe5b9a18cc1b27d190a342e6fc3b89eef0b58f96f5970c0e51bc1", # [icssvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "37b03bf04b5c939fb9733b6d6b9189ad218d86b2cbdd3060105f5021c4c126d6", # [InstallService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d6fe2c22924124da85340b5957493fa8a7fd6188a5e48263b6ba5c8243693917", # [IKEEXT] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "56270e90903b81fb3dc1973256a553e08bdf56ba7ef41d5653955099db7f7478", # [IpxlatCfgSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5ced36aa3255ce4a9868a9861cb0724f7370cfbba143963e997ba5fa4d746c65", # [KtmRm] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6a8031c0ed97307db183552c66253257702d208a425129d51bc1228ce2085b98", # [iphlpsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b78c7e8d9379559452891eb3812dcf6165d6829aac62cb1fff70f70c12825f8b", # [KeyIso] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9d19120467d49b11d504284f1fe65347fc4e70cfa221797ea15aa07888e4cc1d", # [LanmanServer] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "39f52dcc27580db6282ea884a7009f42ac7ec8e47996b9d8b9ca4d26b87b1e5f", # [LanmanWorkstation] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1dcf6fb0aeb607edf6059a463749d92ba36bcbfbc546a5bec349ca9c64b9fbed", # [lfsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d0035aa9c5f49be0d7e99e0d6f640739c73ec27deb7f458355d49cdc31db2586", # [LicenseManager] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "69e04020763664e064ce314bd8309261843a4889276a62f0a28296d8cf8a8503", # [lltdsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c4e5d39e661e316dec94fbece88a5bde007a32f7c41886434624d53df21dff4b", # [lmhosts] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "22666c7f089d420523e97ccbc13c0f231f52f3c13e9ead816e1f00584cc8c957", # [LSM] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e290027ab956038a58faaeb23fbe339c24248b4ee1132779962e1cba2cdfe769", # [LxpSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "ceb71cb7bddc55ad0464a4e7fc8f0817cf53ec3a93eec5c27a1d608d5f269bbe", # [McpManagementService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d19ee321212810a58bb8412c11441672d3ca2c9624f3294f76488af3ad52122b", # [MapsBroker] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6ee42826aa1ad69018144df438b7e927d9f382fbe22c1f4235ff12ba42e09a1e", # [MixedRealityOpenXRSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e583e853751e508a89c6ce6aa6c3e8c454c110e48d376862513c3bd95a8d8837", # [mpssvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a809fac24d5be999fa278c35c3705907f0fda97ad410b2373666206629142b59", # [MSDTC] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3e9f9314c8cdb95bf4092f75db787dc8edd0b9633d5732b54665a5d728451577", # [MSiSCSI] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d466e6bbdd7d2e5d37c2a07a761db757d325c7b836f194c65a4241fcf837a026", # [msiserver] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "94be326943964e040b4e8acf5c0201a57a45ab4665b4f372da69479dee225ef8", # [MsKeyboardFilter] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5e7e08a97073ea6763864c85c55eac63ad88686e56930754290274471d9f0781", # [NcaSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8152f3b046e9daed2028a8d971f7de1fb8f234c553fbf77665d2e7b31d30ba0f", # [NaturalAuthentication] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "072b596fe2a63a3632842194597bce243216d84fd0d24b672905ead70099c591", # [NcbService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6001dffaaedca21ebcffa7a82214829f328dade33dc2562f06d28cd927e0ab01", # [Netlogon] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8991f5b2db5ed33f68536b6ba2246177a58451f01a6107598a7988e9febe1043", # [Netman] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fec4bd91863ba33168f5dd178c918c7248f1c76c000855f23190d84f0d0f2cc9", # [NcdAutoSetup] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2d83f5b6000e56b0eb0851d450c9fd88b78f9269e5669eb6ef4d303e2b8aaea7", # [netprofm] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e5f939930ea07afa0816aba2fe96ee3f2f6693a869620053c96e3079aa9633d8", # [NetSetupSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "45a94a671e0af8f6d2cf81d59cc50f1b5d7e559642bbc96186978a6c456c763d", # [NetTcpPortSharing] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5dbe03e80f96be030fb4fb54e5bed671cc4e7ad953cb012d39fa8a0a23b87a0b", # [NgcCtnrSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "672c53bf5e38e0529e4511c20d7330acea411638072f03874cf0a3781b4de4e5", # [NgcSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "56fa1abf94311fb04720b8479d9e8d5cd39232af0f89b828f12eaae3ce647891", # [NlaSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f278a499a2dd5b7dd17c1126c4e2b4e55801f2e426f630b94c69285cb059fef5", # [p2pimsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b7b88b0c808ffb92f58d527af970bed3d0d0646d52b10fdb03119661e5ce87f8", # [nsi] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7ff0f395d548a1d3c00073b9879ad637a1c7dc8fcb51cdd239307e65e20c68b9", # [p2psvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "116db003a7c13cf943a364ba3b9e751940843ad42ee8db6c0fb5e2762ae30a81", # [PcaSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "35a3342499e7c24ad373232704350b4437643a08a009075275787ccd54d2ffa3", # [PeerDistSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a94cb440f50a267f25a13b951a516e1f32b2d471ef867fd00311604aa1896db7", # [perceptionsimulation] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "849f074dc44290d35663c7e5fdc7bad84e578663d45a1b91cecb817c6367b47f", # [PhoneSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6e1684ee96a6dabd0b9f16de660470234e2c41ebcc30a65ee5e17f8373a8aeff", # [PerfHost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9468c9dd1c0164dc0250eb86a1f05e3db1f1962fe079741251e1d2770bb4d190", # [pla] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b7d199b5169734e9d3680e9aca500f4f387b30721e80cbc46cb856b2b38ede91", # [PlugPlay] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "105ac923a6cb0ba67a5f69868ef92bf38cad8d576155eaa6b5faf4baef292ca9", # [PNRPAutoReg] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0ac589834cb3330f6a0ea80a086ca6beb0d511bfa13ca74fe446a91317a45d0b", # [PNRPsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6b131585b3ef8408c72d69c625a48a12d28b05f15e4dcd1738272ae6ce6c0e4a", # [PolicyAgent] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "848e96567d6b48d54c0b53017bd6123cefa97d6e0fab0f14c621ec3fd92178f4", # [Power] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8055dbc306c6f6664c840693e186f993d9edb7485baeb432f1d0266ed8c75f6a", # [PrintNotify] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "dd20a082458fcec7200ea7a401552f3cf8fdb1f20c0c369278f68dbb68c12c66", # [QWAVE] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9f619a7cc54e97e9d8506bff077ad30598469983ef9289ce2e4e9e2588b865b1", # [PushToInstall] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "097098cffc3e7fff75252b5e701296d9aa590388649dbd2bb33e74de35149175", # [ProfSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "198f4d18671850a7ffeddf7eec789fb64e82f036b2246b19b6d1beeb4eba260a", # [RasAuto] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9c0154922668f1646bf7f2ebc52ac7f26ff0d16170abdea91a64496154cf6442", # [RasMan] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f11a34cdc70de35d432b255785683b6ac3aa3d9bd722e0318d6ebe22e45c15a0", # [RemoteAccess] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d2f28d1fb7c1e4e531568d7ff469ee8147cc25c5b0c19daf4ade557bc20065b6", # [RemoteRegistry] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "da61d944989aae330709cb17f37ff6b645bfb0cda9184015436133e3e01a7caa", # [RetailDemo] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9f1f175fbef65815224f6300134006c02d361190b017cec3f5f6ceefc2fb231d", # [RmSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "95f784eaa97d0bf667a2d7a671d3e08d742015eff354425b6dc6a7ddf840ffd7", # [RpcEptMapper] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fa9ae1b310a4139a0dffc2fbe9f1a43f122969466e0cc5841377f84671219c24", # [RpcLocator] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "391b98e60719fd9212af3aa764c62f92fe2c576d2803213ec101c31b657ada94", # [RpcSs] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0eb2e8428dc8764c54f915119194a16e8d78cce5461a2f2041a61b839d91b6b4", # [ScDeviceEnum] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "db2c4d02838ad387a5097505d191059521d5c9c9e0288924650c5f07bfcebf3f", # [SCardSvr] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "65ff59eac993191cd8b09e8855b9916909c367ffb836993fa16476931f275d52", # [SamSs] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f4830a1dae2980447c716bd4b5779b7013575ef09f70ef4731457218792487b3", # [Schedule] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fe85e1d3c30e5de4c246b05cf1dafeb1b7af942319c89f3a57a1408edd466944", # [SCPolicySvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c81d81f9946d97454c3780a52b39a43c15f9d87217a061bbbd6baada815eaa67", # [seclogon] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7ec2fe9d3e01932121bb132e24f339abffd0e02b7c2be95619e634d85f7c91b6", # [SDRSVC] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2c874233ad1d5c75c0b543e1c68d2146817c4c89b81789cd0c65ed838ee3c848", # [SecurityHealthService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "abea56ac6750974eb8460eb2069b8d19fff1d3c22cb30eecd4f42aac9c371a35", # [SENS] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6857eae79c27f6c24f7aa925176e4024668b0636a177eae2dcea88c40c939ee9", # [SEMgrSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "04ce8d65f2b009969733ddbba9aec182a4e1981feef244760d74131570c51c6b", # [Sense] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "659fb444e06870e4e027a46d32f9c2577377997cf9ec4f7f6cb659be3c4511b2", # [SensorDataService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : BBD2C438000344F439BFDFE5ABAC3223357CD67F
    "87de998b23881c659ae489d188a73ec49edb39042cecd5585f638645ef719f69", # [SensorService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f93c4ac9562dbf181976820be2e2d97d7884fb244b6e7e3c70a7571526c27958", # [SensrSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "de649e45ba446f19c93f794e8d8e48fff878fd07e2a599cec8e6b34eb9bc7980", # [SessionEnv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9d9abc6fb3ae00713d9f21db4da900810d19afcccae69c178d05208d90b98ed9", # [SharedAccess] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b3e8e6cef23deca1c92dbb42ccf342f918f609807493165b97da4cc1eb99bd45", # [SgrmBroker] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "09fb08bb5a89c0640e71f7fb19d1c455c3b2e6453c33d3bea777bec179c36f66", # [SharedRealitySvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9790ab83e503e24fee1ebf0207e4761e24756e78164f38d0bd0c03f36e36b5a2", # [ShellHWDetection] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "09ab19e3b0d7fbc52c2331baab85b1d8d90b84904eb9ad194391226c98a6dae3", # [shpamsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8a7cb4594b985e13af418de80d17010e9496fee61a4c35543b6ddebdf98dc904", # [smphost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "596471bcf2c7c1770e89abab468b0af73861ced04d8f0adfbf3f7d4a9026eb69", # [SmsRouter] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9668a9dd2cb98ab2b073600f375a3131ac5fc8924391e4100e1ce55cb7442c2f", # [Spooler] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d772c858269cf2e4923747c4efa39a0214e3dae0d90ea5126291cd44f6f8a92f", # [SNMPTRAP] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1fd6202c9bb335c65040575f892b4b9269651729adf08036bf11bc4694d9421d", # [spectrum] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "572fa6dfd122138a51695a4e1afd7519a62e37d6b717b1a0753fe770c5da9ce6", # [SSDPSRV] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "13cdfa07bdf8db8bdcfe99eea4b7b1ab2a73d8f0b7d0e0d5f4f9a31bd7f587f8", # [sppsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "92347a6478c92b02932f4815de823614465c5564ea44d3de1f161f4346ad153d", # [SstpSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "ff073805011ee1e103e6acbdd222b731a1752d4db8b8b02c1c41c50664bdc5fd", # [ssh-agent] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : BBD2C438000344F439BFDFE5ABAC3223357CD67F
    "47ab11a0b4f0d265a1937136f3c43551cde0176f73bbf8131fcf13c5052e4e9b", # [StateRepository] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "061b5f6148e44384498c3dfb8a351814957dd4967bacc4f68b3bfc7a5af63dbe", # [StorSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b86bcff64d7ce059f07d2a9cd81f727a942fee4471d55608b68fdcf15e0c26af", # [stisvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e11a6a1a2dead13634f93c55652e94dbc76ad38c5b169c39844736afeccf5d1b", # [svsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4406ee7f13f22fc0fbcb35a0e18d7a8d9a40798c6b4fdbdc886b030f2d0d4fbb", # [swprv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0cf43ae20f0dbc7ceb23cce2ab0328d77573e36b389d8ce5716fb7e8b4b2932d", # [SystemEventsBroker] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "58d782c668e2819a2b4deebd227e93b543ebff14fa3495c6e24866cc0256e238", # [SysMain] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "618efc15ec459533323677c3b33d87c9981a294d8d82050a2380f79ff3d6f14f", # [TabletInputService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "43ae3265b99f2f34e9079ca3e2241ca8729718d749b3eaa2a616628dc2d2f751", # [Themes] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "29547ef3b86b340824f71a8a31e12cb0bead16ff0e26583bba1944546e24f285", # [TieringEngineService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1fd589d8babbbc5a2c1d5aa9d3ee2f67f3fc5d7410ae57df3fc2a2dbf612bff9", # [TermService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e1568133cd44f9fca3a5ad658e6158326fbcd40180c2560e461ac936786a45b5", # [TapiSrv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2257c2fe2362fa576e54048d6f506b82b74b687ea5f69d0a714b699a78a60bac", # [TimeBrokerSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "5ae593794d3faf83f2603a20ed30d592f6e15ab4bc07f1513f5f436b25f7a780", # [TrkWks] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6c37769578672f12864912fd106c8cdfcbf20653040e888af7ee2e7bee03e8f6", # [TokenBroker] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f7c60d9fb2200c05032cb2dddc4617f31340c335e6c396cf867e1b5daa7ec066", # [TroubleshootingSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c2a40e7038b5c97c835109d606d151c9e05250060469d738126207b8fccd7541", # [TrustedInstaller] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7453efe26bbf6a635758b18c2e7d4ea2f07ca6d1c6ff84663610bce6e5a58ce3", # [UevAgentService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8c24a45b645a0aae4df294c291017366a4245b87d8ba3970a3356b4dd762ea26", # [tzautoupdate] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f37ff10c230b287833313b0bb27348cf5795a136c5575787852fd551e7303c4a", # [uhssvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 58FD671E2D4D200CE92D6E799EC70DF96E6D2664
    "76c1757d805d913d350f012a4ada2254301e2b58489dac8c22150fab27085687", # [upnphost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "26a6f0d8066419599e6c414dbfc8e27ea084369b22a2523a338542716df45361", # [UserManager] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3e6a524914d418992b6da879a3bcf479f53a9ad7e9f4e19a35859f71c5b48df9", # [UmRdpService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c8dacf7158f8ab41b92b5f210eadf6226bcfa645e2ca15eebe809dd67ebb3515", # [UsoSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a4df6b4e5202ca6d1758b679191b135891df6329e1a7acab59274ff243ea9ad1", # [VacSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f186e778a7ce4df37ef5eabdcd8d3d9ed8ed27c7bf540834db6448cd0367b2d0", # [VaultSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7aefa2fc34b5a9391fe4c5702c121d462fb601906d76365db930a8b612c79ac6", # [VBoxService] - Valid Windows Service. Issuer : CN=DigiCert SHA2 Assured ID Code Signing CA, OU=www.digicert.com, O=DigiCert Inc, C=US

    # Thumbprint : 30656FCA8C48B1D98623A94B40A6BC98BD87BFAD
    "810cc6914d7cb6597a0020b6e5aec82f1cfe6370bb93a816eefb1b6e09da9ff0", # [vds] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d7e04f974ab49593b1d0fe6101b994353d96e864e53e7c49fa7c84c5ea7afab4", # [vmicguestinterface] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b27c47bc9b0984e4872057a8de64e0382510676dd20130f310e08dacff507ca9", # [vmicheartbeat] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e8b1d01d8ccecacb755f2ed20b3324757d22b654fddc9003c43d9f0b191ddd22", # [vmickvpexchange] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "abb671f98f8c46d77764997dd9d12227ac991f48d5652bd7a5b6045aa4cc4f35", # [vmicshutdown] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8e7257de19fca1ee18d0034a58846a62b23c4a357494105fd27f52ab12af753c", # [vmictimesync] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c11c1757e0a85c3b7d4d03ef19d2e34eb711cb084e679eaf1d342ad46d887268", # [vmicrdv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "776f8045e4d6226dd271f51c45d181a8a3a9a637005ab8066a13406c2063ff62", # [vmicvmsession] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fe92451c47e2192835de8561681c2c195be4bb43d52836b62b458b15f1d68084", # [vmicvss] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c4dcd1cbb606759213386a674b2820fe8226c56ccec7362cd5d71b5600930eee", # [VSS] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3268b498f52d3843037e6849625f130f5bee222afc2a296fc81b71290d544a4a", # [W32Time] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d45f47622464cb855d7ec31b78c2c26249dbe3fe27c9682cf673be49d8cc4d50", # [WaaSMedicSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a8af982004a604edeb65f4a0902e0a93ce45eec59c763bea2770d3fb667d3cc4", # [WalletService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "fca138e4c59a82ee402e6ec089915b0aa6c889deba8179f3203b5c44fa71506c", # [WarpJITSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a096c58f9498cd781135393007b428461e424b403a78590cbfbc81c46cd51133", # [wbengine] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "90c6d2bc6beaeb92ba81797bdac51c52aef6fe9bde6e3f923c9fec5dd4d6f35f", # [WbioSrvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9708c0fc8af1e521516d1a17cb6f6f03db0019fd93f3627505f8c526ceee3924", # [Wcmsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3b5811a289646831718512354afa8aa991dbe44df2a7ce83e508a231a442d6c3", # [wcncsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d7f5b2fbaef34c27d1b4eed9d0fcd7882c3470f26c9d938cf9839e93aaf0b1fd", # [WdiServiceHost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "616183dc7761659970b3c18d4111eebbe155218030163aa38191226fbe4a17a3", # [WdiSystemHost] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "2cbf9520b29b3f1cbe780385db201a68fd038300bbf8c76ac1b91c06eef7d1ad", # [WebClient] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e2b279c07f9b937f3efcf29c444563bc55dc5d629bcbab4dc14d907ff52825e4", # [WdNisSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 86460D89EE50F8BEF728491C3C8C759369F12E76
    "8dde34aca062914513827225340d62d5de849debbd7bb6aa158ab67a10287489", # [Wecsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4c4747dd893d62e05271698f196aed4c194447de2f15d6112da4c1c62e140ad7", # [WEPHOSTSVC] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "065d253a5e1db4d8636b63b2b5492dd5441f26d1f7ac246fd4ae80e8745b4dfc", # [wercplsupport] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "987a86f43222892fcb946486bc8ba557aa4a1b3dd6795e82477e25c949b9c5f0", # [WerSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "efa2027cf6a4d424948ae40e2d79bd3cb05c95c4a45b62bad330c199622214df", # [WFDSConMgrSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "d5be40d7451583a3c6e4f86e8e0291cb1e7fd55ae1b8a248675b81f5c9e4b82f", # [Winmgmt] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1ed30fb81257ebbf8fee75a9e2ccb894f120f91a9903174aa6b92077d65e4c89", # [WinHttpAutoProxySvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a579057d2f1d73fd057c644bc8ca0a6ddd7b1143c9cbbaa5063efe13ea450c7b", # [WinDefend] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 86460D89EE50F8BEF728491C3C8C759369F12E76
    "2de77b804f67146feb3db561a04e3cc5226c37612edc2c0e9c682dd2179c4d16", # [WiaRpc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a84920d37bc8ffb1213bc47ced9d6bf84f5770b840b0c0570f72b23b9034e00a", # [WinRM] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "ea16cf5d4dd7445a350369143a01e69b694f198c2461e25bc7d25c9b50814f19", # [WlanSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3a136bd8a2124123eda58f8502da0c85258ae1bf2b4de68ada878436caf8827d", # [wisvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "757a1df4ce25d2aac5d17d713533e920a51f9d121f2327934796072daae90307", # [wlpasvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3e9fb1d3c45778fb50f3b9ee9920b06d15f5d8c1c2049742cdd6cdcd28b9b497", # [wlidsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "368c2ef57f34521cd477b90b1bb121774631f4346469cecf9fac26bd026233a1", # [WManSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1827c8cbeb22693133d49b3cbf5bba014bbd2b3828ede765ab0fff0d93bce2ef", # [wmiApSrv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a218ca1bad5b31bfb8892453a612baf22a7eeb1ba57a9926825423138a46dd62", # [WMPNetworkSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : FE51E838A087BB561BBB2DD9BA20143384A03B3F
    "67741ada8c48cea24ef72a241a682da6a48751747bd7ac4778b42de5b3c37a31", # [WpcMonSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "bc9e073240a374590c25b00ddd62c95aacfe49a4d8e26e361b7b0f50b0b99ef5", # [workfolderssvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4f002fee82191eee34a36d2d75078e86c65837ccfb53822f4cb41697dd4faa9d", # [WPDBusEnum] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "31ada3f1df10fdb47d27fb22c5bde51b5f18f50ad8a634cfffea02ae318d5b23", # [WpnService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "878dec2182d4a7bef6e7a7e2f707f9084bae79015a16e5afbfdee9106aa5b63e", # [wscsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a94ea05552c969e0e4bffb5d82389093f830d483a9a9a1db04f57af3409eb087", # [WSearch] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "29d36de5355adcaf04a3cdb27fc3f19c63fe9c58f612b31ae31f99b94f234872", # [wuauserv] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "bf7a26ea800740456554581e413b617b03730392c72a85d9ad3071384aae37f0", # [WwanSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "0ca8fcff49dd5ba525c40dbd3bd165c18081d694d960f5768603ef923f7e82de", # [XblAuthManager] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "6fc0bdecbe268877bff4f5243387e48f452f5601398acfc653676244ba0e7573", # [XboxGipSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "8b5dd3413f3fed926b8b13317baed12b42d01556c4fac981873415647f981e32", # [XblGameSave] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "7bc74fc31c4611dec70a6256fa763d94dfc7adddb93df27991f25f68402f5ac2", # [XboxNetApiSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "aa1409da1b765c67a9e4c8b24387d51cd891dd7a16106340134deaee9028b160", # [AarSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "1f923302f81475de18255b7b9c2c7547f4be0504e2e3aed67547201fcdd0dbef", # [BcastDVRUserService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "e678676d73a3d39abe4734d5e8d3b3bb347db93564081eaaf5cbaece4a261457", # [BluetoothUserService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9648c7db0707f60b5e48b82ba7cdfbc6daf7a4c0e3b132449afeee362287c903", # [CDPUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "4b8e41868d9987954f9c351c6ce13eb6a68aca241d67004f8d1729aa5d7beed7", # [CaptureService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "af097fba8ecf48d198454be7f002fa567f5c7ceac324a6b8dd254da57f90e67b", # [cbdhsvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a313e2650fd5d74a81b789a9052aaa1931aff147139dc89f1cba6aefca421814", # [ConsentUxUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "08e8f0e7f7ae16c34179bdafe6af4d0e06c5fb341f04fa44b700201bed5e2294", # [CredentialEnrollmentManagerUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "40cbb02f6dd62db612348aaff1c262c2b09c0907a0c0d36bd44df9b2be800efa", # [DeviceAssociationBrokerSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "821737a90725db907a76bac569f7420242f7527a4a68fc1e367ebb303a6b72b7", # [DevicePickerUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "3cc52f823624af9ba78d66098f4a5959b06ede79f49db20340930db612985867", # [DevicesFlowUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c27f0b1bdc0ae7f532afab2573f1fe3e85e6e73e67086a9bf3eee641f10ab178", # [MessagingService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "b79f53f918251409dfb720297303b5f9be97330cc948eb75fc7598a4eb2911d4", # [OneSyncSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "f92f3597e3e54ed095a060a5f74d1892eb575f8d091e953d2162dff0df195c04", # [PimIndexMaintenanceSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "a0b0d38d41ff759c24440595239be45a8f90334d42b4b81a9e384081521ebf36", # [PrintWorkflowUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "9ae44f7b7ea4ceb6c37fbe263a18f2716fdda80dea073296baabc8ca87bd5cf4", # [UdkUserSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "97577d89e704a9ee4d865ca0d579aa0334df4ca723fdafd28960e4e582132866", # [UnistoreSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "c6fd23092c8092146f8bb4f8b3971de6bedc1969a1e380f51ad4fa3718f19814", # [UserDataSvc] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

    # Thumbprint : 8870483E0E833965A53F422494F1614F79286851
    "20bfe703b8f5c2f4f132502bc9920674c7dac3f2b00d89290121544fcc82ee4d", # [WpnUserService] - Valid Windows Service. Issuer : CN=Microsoft Windows Production PCA 2011, O=Microsoft Corporation, L=Redmond, S=Washington, C=US

]