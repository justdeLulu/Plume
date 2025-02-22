-- CreateTable
CREATE TABLE "rules" (
    "id" TEXT NOT NULL,
    "power" INTEGER NOT NULL,
    "name" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "active" BOOLEAN DEFAULT false,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "updatedAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "rules_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "ForbiddenWords" (
    "id" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "word" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "ForbiddenWords_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "Mistakes" (
    "id" TEXT NOT NULL,
    "content" TEXT NOT NULL,
    "createdAt" TIMESTAMP(3) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "Mistakes_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Mistakes_content_key" ON "Mistakes"("content");
